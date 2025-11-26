from django.db import models
from django.contrib import admin

# ---------------------------
#   Customer Model
# ---------------------------
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

    def __str__(self):
        return f"{self.name} - {self.account_number}"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'name', 'age', 'email', 'phone_number', 'balance')
    search_fields = ('account_number', 'name', 'email')


# ---------------------------
#   Bank Employee Model
# ---------------------------
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

    def __str__(self):
        return f"{self.name} ({self.emp_id})"


class BankEmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name', 'position', 'salary', 'branch')
    search_fields = ('emp_id', 'name')

