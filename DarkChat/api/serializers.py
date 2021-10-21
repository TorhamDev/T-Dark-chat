from rest_framework import serializers
from api.models import Validـcodes, Messages,User_code


class ValidCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validـcodes
        fields = ["valid_code"]




class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["message_text", "sender", "receiver", "date"]


class UserCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_code
        fields = ["username_code", "create_date"]