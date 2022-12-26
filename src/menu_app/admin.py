from django.contrib import admin

from menu_app.models import Menu, MenuItem


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ['name', 'slug']


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin):
    fields = ['menu', 'name', 'parent', 'path']
    list_display = ['menu', 'name', 'parent', 'path']