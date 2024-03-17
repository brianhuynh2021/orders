from django.contrib import admin

from .models import Category, Customer, MenuItem, Order, OrderItem, Staff

# Register your models here.

admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderItem)
