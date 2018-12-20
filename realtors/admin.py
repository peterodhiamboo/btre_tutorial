from django.contrib import admin
from .models import Realtor

# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'is_mvp', 'email', 'hire_date')
    list_editable = ('is_mvp',)
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
