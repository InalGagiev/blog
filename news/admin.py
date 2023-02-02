from django.contrib import admin
from .models import *

#таким образом мы добавили таблицу News в панель админа
admin.site.register(News)