from rest_framework import serializers


from .models import Course, Subject, Teacher, Student, Profile , StudentRegionNorth, StudentRegionSouth

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Teacher
        fields = '__all__'  
        
class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Student
        fields = '__all__'  
        
class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Profile
        fields = '__all__'  
        
class StudentRegionNorthSerializer(serializers.ModelSerializer):    
    class Meta:
        model = StudentRegionNorth
        fields = '__all__'  
        
class StudentRegionSouthSerializer(serializers.ModelSerializer):        
    class Meta:
        model = StudentRegionSouth
        fields = '__all__'      
        
