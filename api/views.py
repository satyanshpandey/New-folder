from django.shortcuts import render

# Create your views here.
def students(request):
    student = [
        {
        'naame':'satya',
        'class': 'first class'
    }
    ]
    return render(request , 'students.html' , {'student':student})