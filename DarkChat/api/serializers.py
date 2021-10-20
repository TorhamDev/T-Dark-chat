from rest_framework import serializers
from api.models import Validـcodes, Messages


class ValidCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validـcodes
        fields = ["valid_code","is_valid"]




class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["message_text", "sender", "receiver", "date"]