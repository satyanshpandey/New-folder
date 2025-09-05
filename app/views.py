from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def students(request):
    di1 = {
        "Name": "John",
        "Age": 22,
        "Course": "Computer Science"
    }
    return JsonResponse(di1)
