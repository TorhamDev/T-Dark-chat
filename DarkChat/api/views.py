from typing import Counter
from django.shortcuts import HttpResponse
from api.models import Validـcodes
from api.serializers import ValidCodesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random
import string
# Create your views here.

def index(request):

    return HttpResponse("hi :)")

class GetValid_Code(APIView):
    '''
    return a valid code
    '''
    def get(self, request, format=None):
        while True:
            letters = string.ascii_letters + string.digits
            random_code = ''.join(random.choice(letters) for i in range(25))

            if Validـcodes.objects.filter(valid_code=random).exists():
                continue

            else:
                valid_code = Validـcodes(valid_code=random_code, is_valid=True)
                valid_code.save()
                break

        return_code = Validـcodes.objects.filter(valid_code=str(random_code))
        serializer = ValidCodesSerializer(return_code, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)