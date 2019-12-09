from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.


def test1(request):

    return render(request, "demo1/text1.html")