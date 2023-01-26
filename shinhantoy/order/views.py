from django.shortcuts import render
from .models import Order, Comment
from rest_framework import generics, mixins
from .paginations import OrderLargePagination
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
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


class OrderDetailView( #detail은 하나 ex)하나만 가져와줘, 하나만 삭제해줘
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    serializer_class=OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id') #urls.py를 통해

    def get(self, request, *args, **kwargs): #포스트맨에서 보내는 method
        return self.retrieve(request, args, kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)


class CommentListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    generics.GenericAPIView
): 


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer
    
    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        return Comment.objects.filter(order_id=order_id)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
        
