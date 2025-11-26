from django.contrib import admin
from .models import Customer, CustomerAdmin, BankEmployee, BankEmployeeAdmin

# Register your models here
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankEmployee, BankEmployeeAdmin)
