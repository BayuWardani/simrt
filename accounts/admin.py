from django.contrib import admin

# model dari app
from accounts.models import Account

# admin 
from accounts._admin._accounts_admin import AccountAdmin

# Register your models here.
admin.site.register(Account,AccountAdmin)