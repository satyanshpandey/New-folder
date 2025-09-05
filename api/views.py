from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Simple function-based view
def students(request):
    stu = {"Name": "John Doe", "Age": 21, "Course": "Computer Science"}
    
    return JsonResponse(stu)



