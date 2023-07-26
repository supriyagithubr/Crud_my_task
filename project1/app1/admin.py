from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['o_id', 'o_price', 'name', 'o_date', 'product', 'add']
admin.site.register(Order,OrderAdmin)