from django.shortcuts import render
from .models import Order
from rest_framework import generics, mixins
from .paginations import OrderLargePagination
from .serializers import OrderSerializer
# Create your views here.

class OrderListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)