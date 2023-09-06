from django.contrib import admin
from pdfinvoice.models import invoices, Employees
# Register your models here.
admin.site.register(Employees)
admin.site.register(invoices)