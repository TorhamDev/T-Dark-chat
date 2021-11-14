from rest_framework import serializers
from api.models import Validـcodes, Messages,User_code


class ValidCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validـcodes
        fields = ["valid_code"]


class UserCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_code
        fields = ["username_code", "create_date"]



class MessagesSerializer(serializers.ModelSerializer):
    sender_user = serializers.StringRelatedField()
    receiver_user = serializers.StringRelatedField()
    class Meta:
        model = Messages
        fields = ["message_text","receiver_user","sender_user","date"]
