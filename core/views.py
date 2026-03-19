from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('Django API Rest Framework is active...')