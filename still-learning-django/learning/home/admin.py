from django.contrib import admin
from home.models import Prod

class UsersAdmin(admin.ModelAdmin):
    list_display =('id','name','brand','product','price','quantity')
    list_display_links = ('name',)
    search_fields = ('product','name',)
    list_per_page = 15

admin.site.register(Prod, UsersAdmin)