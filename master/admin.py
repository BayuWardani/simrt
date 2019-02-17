from django.contrib import admin
from solo.admin import SingletonModelAdmin
from master.models import *
# Register your models here.
# class KonfigurasiSistemAdmin(SingletonModelAdmin):

admin.site.register(KonfigurasiSistem,SingletonModelAdmin)