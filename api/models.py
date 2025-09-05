# from django.db import models

# # Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
    
#     class Meta:
#         abstract = True
        
# class Course(models.Model):
#     name = models.CharField(max_length=100)
    
    
# class Subject(models.Model):
#     name = models.CharField(max_length=100)
    
# class Teacher(Person):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     subjects = models.ManyToManyField(Subject)
    
    
# # Student
# # Student
# class Student(Person):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     subjects = models.ManyToManyField(Subject)

    
#     # Profile (One-to-One)
# class Profile(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     age = models.IntegerField()
#     address = models.TextField()
    

# # Employee (Self-Referential)
# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

# # Example: Horizontal Sharding
# class StudentRegionNorth(Student):
#     class Meta:
#         db_table = 'student_north'
#         managed = False  # We'll manually manage DB routing

# class StudentRegionSouth(Student):
#     class Meta:
#         db_table = 'student_south'
#         managed = False









from django.db import models

# ========================
# Abstract Person Model
# ========================
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name  # For inherited models like Student/Teacher


# ========================
# Course Model
# ========================
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ========================
# Subject Model
# ========================
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ========================
# Teacher Model
# ========================
class Teacher(Person):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.name} ({self.course.name})"


# ========================
# Student Model
# ========================
class Student(Person):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.name} ({self.email})"


# ========================
# Profile Model
# ========================
class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.student.name} - Age: {self.age}"


# ========================
# Employee Model
# ========================
class Employee(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# ========================
# Horizontal Sharding Models
# ========================
class StudentRegionNorth(Student):
    class Meta:
        db_table = 'student_north'
        managed = False

    def __str__(self):
        return f"[North] {self.name}"


class StudentRegionSouth(Student):
    class Meta:
        db_table = 'student_south'
        managed = False

    def __str__(self):
        return f"[South] {self.name}"
