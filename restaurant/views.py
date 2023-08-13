from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')

 from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})