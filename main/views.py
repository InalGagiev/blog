from django.shortcuts import render


#это функция с главной страничкой сайта
def home(request):
    return render(request, 'base/home.html')