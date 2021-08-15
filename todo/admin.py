from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    # columns shown for Todos list in admin page
    list_display = ('id', 'title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin)