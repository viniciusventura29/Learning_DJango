from django.contrib import admin
from home.models import Music

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','author','bpm','tom')

admin.site.register(Music,UserAdmin)