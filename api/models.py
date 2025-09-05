from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        abstract = True
        
class Course(models.Model):
    name = models.CharField(max_length=100)
    
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    
class Teacher(Person):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    
    
# Student
# Student
class Student(Person):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    
    # Profile (One-to-One)
class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()
    

# Employee (Self-Referential)
class Employee(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

# Example: Horizontal Sharding
class StudentRegionNorth(Student):
    class Meta:
        db_table = 'student_north'
        managed = False  # We'll manually manage DB routing

class StudentRegionSouth(Student):
    class Meta:
        db_table = 'student_south'
        managed = False