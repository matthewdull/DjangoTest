from django.http import HttpResponse

# View is just a function
def movies(request):
    return HttpResponse("Hello there")

def home(request):
    return HttpResponse("Home Page")
