from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def say_hello(request):
#    return render(request, 'playground/hello.html', {'name': 'Django'})
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Django'})


def say_hi(request):
    return render(request, 'hello.html')
