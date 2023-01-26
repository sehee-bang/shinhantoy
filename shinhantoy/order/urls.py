from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view()),
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/<int:order_id>/comment", views.CommentListView.as_view()),  #사시에 <>이거 넣어주면! product_id라는 변수로 받을래 !
]