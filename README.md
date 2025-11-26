# Ex02 Django ORM Web Application
# Date:26-11-2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM

admin.py
~~~
from django.contrib import admin
from .models import Customer, CustomerAdmin, BankEmployee, BankEmployeeAdmin
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankEmployee, BankEmployeeAdmin)
~~~

models.py
~~~
from django.db import models
from django.contrib import admin

class Customer(models.Model):
    account_number = models.CharField(
        max_length=20,
        unique=True,
        help_text="Customer Account Number"
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def _str_(self):
        return f"{self.name} - {self.account_number}"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'name', 'age', 'email', 'phone_number', 'balance')
    search_fields = ('account_number', 'name', 'email')

class BankEmployee(models.Model):
    emp_id = models.CharField(
        primary_key=True,
        max_length=6,
        help_text='Employee ID'
    )
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.name} ({self.emp_id})"


class BankEmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name', 'position', 'salary', 'branch')
    search_fields = ('emp_id', 'name')
~~~

urls.pr
~~~
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
~~~

# OUTPUT
<img width="1365" height="638" alt="image" src="https://github.com/user-attachments/assets/9b75036f-ac28-4e3d-84a0-1dc1626651bc" />



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
