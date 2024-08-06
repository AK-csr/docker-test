from django.http import HttpResponse

def home_page_view(response):
    return HttpResponse("Hello, World!")
