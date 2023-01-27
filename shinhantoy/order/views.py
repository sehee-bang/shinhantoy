from django.shortcuts import render
from .models import Order, Comment
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
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
    generics.GenericAPIView
):
    serializer_class=OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id') #urls.py를 통해

    def get(self, request, *args, **kwargs): #포스트맨에서 보내는 method
        return self.retrieve(request, args, kwargs) 


class CommentListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
): 
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id).order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
        
class CommentCreateView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

        
class CommentDetailView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    
    def get_queryset(self):
        return Comment.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
