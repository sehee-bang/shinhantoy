from rest_framework import pagination

class OrderLargePagination(pagination.PageNumberPagination):
    page_size = 100000