from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")
def contact(request):
    return HttpResponse("Contact")
def about(request):
    return HttpResponse("About")