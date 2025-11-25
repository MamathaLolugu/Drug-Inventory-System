from django.contrib import admin

# Register your models here.

from .models import Drug, Movement

admin.site.register(Drug)
admin.site.register(Movement)
