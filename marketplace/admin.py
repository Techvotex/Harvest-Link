# marketplace/admin.py
from django.contrib import admin
from .models import Product, Inquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','seller','price','location','created_at')
    search_fields = ('name','seller__username','location')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id','product','buyer','created_at')
    search_fields = ('product__name','buyer__username')


