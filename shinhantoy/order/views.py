from django.shortcuts import render
from .models import Order
from rest_framework import generics, mixins
from .paginations import OrderLargePagination

# Create your views here.

class OrderListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    pagination_class = OrderLargePagination

    def get_queryset(self):
        
        orders = Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
