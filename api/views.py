from django.shortcuts import render
from django.http import HttpResponse

# Simple function-based view
def students(request):
    return HttpResponse("This is the students page")



