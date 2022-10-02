from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def reverse(request):
    user_text = request.GET['username']
    reverse = sum([int(i) for i in user_text])
    return render(request, 'reverse.html', {'word': reverse})
