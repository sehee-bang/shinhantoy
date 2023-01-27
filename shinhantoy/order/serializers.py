from rest_framework import serializers
from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer): #serializer 역할 - 데이터 변환 / 언더바_ 필드명으로 검증
    member_username = serializers.SerializerMethodField()

    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_member_username(self, obj): #두 개의 인자 필요, self는 serializer고 obj는 queryset으로 나온 객체
        return obj.member.username
    
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required = False
    )

    class Meta:
        model = Comment
        fields = '__all__'
