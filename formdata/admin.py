from django.contrib import admin
from formdata.models import Formdata
class FormdataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message')
    admin.site.register(Formdata) # dont pass second argument this will register your model in admin

# Register your models here.
