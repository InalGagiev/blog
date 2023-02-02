from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #главная страничка сайта
    path('', home),
    #галвная страница показа статей
    path('news/', include('news.urls')),
    #Адрес на приложение регистрации
    path('registration/', include('registration.urls')),
    #Аутенфикация
    path('accounts/', include('django.contrib.auth.urls'))
]
