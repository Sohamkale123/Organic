# I have created this file soham kale
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("This is about page")