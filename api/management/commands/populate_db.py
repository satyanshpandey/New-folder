import random
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Student, Teacher, Course, Subject, Profile
from api.models import StudentRegionNorth, StudentRegionSouth
from django.db import transaction

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating database...")
        
        NUM_COURSES = 5
        NUM_SUBJECTS = 10
        NUM_TEACHERS = 10
        NUM_STUDENTS = 1000

        # ===============================
        # Create Courses
        # ===============================
        courses = []
        count = 0
        for i in range(NUM_COURSES):
            course = Course.objects.create(name=f"Course {i+1}")
            courses.append(course)
            count += 1
            print("Created course:", course.name, "Count:", count)
        self.stdout.write(f"{NUM_COURSES} Courses created.")

        # ===============================
        # Create Subjects
        # ===============================
        subjects = []
        for i in range(NUM_SUBJECTS):
            subject = Subject.objects.create(name=f"Subject {i+1}")
            subjects.append(subject)
            count+=1
            print("Created Subject:", subject.name, "count:", count)
            
        self.stdout.write(f"{NUM_SUBJECTS} Subjects created.")

        # ===============================
        # Create Teachers
        # ===============================
        teachers = []
        for i in range(NUM_TEACHERS):
            teacher = Teacher.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                course=random.choice(courses)  # ✅ This is required
            )
            # Assign random subjects
            teacher.subjects.set(random.sample(subjects, k=random.randint(1, 5)))
            teachers.append(teacher)
        self.stdout.write(f"{NUM_TEACHERS} Teachers created.")

        # ===============================
        # Create Students
        # ===============================
        students = []
        for i in range(NUM_STUDENTS):
            student = Student.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                course=random.choice(courses)
            )  
            # Assign random subjects
            student.subjects.set(random.sample(subjects, k=random.randint(1, 5)))
            # Create Profile
            Profile.objects.create(
                student=student,
                age=random.randint(18, 30),
                address=fake.address()
            )
            students.append(student)
        self.stdout.write(f"{NUM_STUDENTS} Students created.")

        # ===============================
        # Horizontal Sharding Example
        # ===============================
        # Let's split students by random into North and South regions
        for student in students[:NUM_STUDENTS//2]:
            StudentRegionNorth.objects.using('north').create(
                name=student.name,
                email=student.email,
                course_id=student.course.id
            )
        for student in students[NUM_STUDENTS//2:]:
            StudentRegionSouth.objects.using('south').create(
                name=student.name,
                email=student.email,
                course_id=student.course.id
            )
        self.stdout.write("Sharded students inserted into North and South DBs.")

        self.stdout.write(self.style.SUCCESS("Database population complete!"))
