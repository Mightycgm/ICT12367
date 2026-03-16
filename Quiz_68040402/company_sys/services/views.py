from django.shortcuts import render


def index(request):
    return render(request, 'services/index.html')


def products(request):
    return render(request, 'services/products.html')


def feedback(request):
    return render(request, 'services/feedback.html')
