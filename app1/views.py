from django.shortcuts import render
from django.http import HttpResponse


def demo_view(request):
    return HttpResponse('hello')


def demo_view1(request):
    return HttpResponse('hello')


def demo_view2(request):
    print(10/0)
    return HttpResponse('hello')
