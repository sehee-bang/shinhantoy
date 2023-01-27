from django.contrib import admin
from .models import Comment, Order
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass