from django.http import HttpResponse

def home(rqeuest):
    return HttpResponse("This is the most first page of Django Framework.")