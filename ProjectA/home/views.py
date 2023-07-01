from django.shortcuts import render

# Create your views here.


def custom_fun(request):
    return render(request, 'home.html')
