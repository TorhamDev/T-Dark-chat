from typing import Counter
from django.shortcuts import HttpResponse
from api.models import User_code, Validـcodes
from api.serializers import ValidCodesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random
import string
import hashlib
# Create your views here.

def index(request):

    return HttpResponse("hi :)")

class GetValid_Code(APIView):
    '''
    return a valid code
    '''
    def get(self, request, format=None):
        while True:
            chars = string.ascii_letters + string.digits
            random_code = ''.join(random.choice(chars) for i in range(25))

            if Validـcodes.objects.filter(valid_code=random).exists():
                continue

            else:
                valid_code = Validـcodes(valid_code=random_code, is_valid=True)
                valid_code.save()
                break

        return_code = Validـcodes.objects.filter(valid_code=str(random_code))
        serializer = ValidCodesSerializer(return_code, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SetUserPasswordCode(APIView):
    '''
    set user password and save in database
    '''
    def post(self,request, foramt=None):

        user_code = request.data["user_code"]
        user_code_password = request.data["user_code_password"]

        ## hashing usr password to sha256
        user_code_password = hashlib.sha256(str(user_code_password).encode()).hexdigest()


        user_code_is_valid = False

        if Validـcodes.objects.filter(valid_code=user_code).exists():

            user_code_is_valid =  Validـcodes.objects.filter(valid_code=user_code).first().is_valid
            if user_code_is_valid:
                try:
    
                    ## save user code and password
                    user = User_code(username_code=user_code, username_code_pass=user_code_password)
                    user.save()

                    ## change is_valid to False
                    valid_code = Validـcodes.objects.get(valid_code=user_code)
                    valid_code.is_valid = False
                    valid_code.save()

                    ## return True response
                    return Response({"status":"ok","description":"User registered successfully"}, status=status.HTTP_200_OK)
                    
                except Exception:
                    ## return bad request response
                    return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
               
        else:
            ## return bad request response
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
