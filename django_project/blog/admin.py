from django.contrib import admin
#регистрируем модель в админ панель/ Post хотим
from .models import Post
admin.site.register(Post)
