from django.shortcuts import render

# Create your views here.


def firstP(request):
     return render(request, 'main/firstP.html')


def secondP(request):
       return render(request, 'main/secondP.html')

