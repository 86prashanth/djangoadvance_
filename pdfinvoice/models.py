from django.db import models

class Employees(models.Model):
    emp_id = models.AutoField
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department= models.CharField(max_length=20)
    


class invoices(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length = 100)
    pay_method = models.CharField(max_length = 15)
    amount = models.FloatField(max_length=10)
    description = models.CharField(max_length=50)
    order_date = models.DateField()