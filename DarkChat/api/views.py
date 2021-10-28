from django.shortcuts import HttpResponse
from api.models import Messages, User_code, Validـcodes, SendToken
from api.serializers import ValidCodesSerializer, MessagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from django.utils.timezone import now
import random
import string
import hashlib



## my coustume function
def TokenCreator():
    '''
    create new token 
    '''
    while True:
        chars = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(chars) for i in range(70))

        if SendToken.objects.filter(token=random_code).exists():
            continue

        else:
            return str(random_code)
            break


def UserCodeCreator():
    '''
    create new user code
    '''
    while True:
        chars = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(chars) for i in range(25))

        if User_code.objects.filter(username_code=random_code).exists():
            continue

        else:
            return str(random_code)
            break



# Create your views here.
def index(request):
    last_hour_date_time = now() - timedelta(hours = 1)
    time_now = now()
    return HttpResponse(f"hi :)<br>{time_now} <br> {last_hour_date_time}")

class GetValid_Code(APIView):
    '''
    return a valid code
    '''
    def get(self, request, format=None):
        while True:
            random_code = UserCodeCreator()

            if Validـcodes.objects.filter(valid_code=random_code).exists():
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
        try:
            user_code = request.data["user_code"]
            user_code_password = request.data["user_code_password"]
            time_for_death = request.data["death_time"]
            ## hashing usr password to sha256
            user_code_password = hashlib.sha256(str(user_code_password).encode()).hexdigest()

            user_code_is_valid = False
        
        except Exception as ex:
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)


        if Validـcodes.objects.filter(valid_code=user_code).exists():

            user_code_is_valid =  Validـcodes.objects.filter(valid_code=user_code).first().is_valid
            if user_code_is_valid:
                try:
                    
                    death_time = now() + timedelta(hours = int(time_for_death))
                    time_now = now()
                    ## save user code and password
                    user = User_code(username_code=user_code, username_code_pass=user_code_password, create_date=time_now, time_of_death=death_time)
                    user.save()

                    ## change is_valid to False
                    valid_code = Validـcodes.objects.filter(valid_code=user_code)
                    valid_code.delete()

                    ## create and set token for user
                    token_user = User_code.objects.filter(username_code=user_code).first()
                    token = TokenCreator()
                    user_token = SendToken(token=token, user_token=token_user, is_valid=True)
                    user_token.save()

                    ## return True response
                    return Response({"status":"ok","description":"User registered successfully","token":token}, status=status.HTTP_200_OK)
                    
                except Exception as ex:
                    ## return bad request response
                    return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
               
        
        ## return bad request response
        return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)


def CheckUserDeath(user_code):
    user = User_code.objects.filter(username_code=user_code).first()
    user_create_time = user.create_date
    user_death_time = user.time_of_death
    time_now = now()
    if time_now == user_death_time or time_now >= user_death_time:
        user.delete()
        return "user death"

    else:
        return "user live"

class SendMessage(APIView):
    '''
    send message betwin users
    '''
    def post(self,request, foramt=None):
        try:
            user_code = request.data["sender"]
            user_token = request.data["user_token"]
            receiver_code = request.data["receiver"]
            message_text = request.data["text"]

            user_check = CheckUserDeath(user_code=user_code)

            if user_check == "user death":
                return Response({"description":"User is not allowed"}, status=status.HTTP_403_FORBIDDEN)

            sender_is_valid = False
            rereceiver_is_valid = False
            token_sneder = False
            if User_code.objects.filter(username_code=user_code).exists():
                sender_is_valid = True
                user_exists = User_code.objects.filter(username_code=user_code).first()

            if User_code.objects.filter(username_code=receiver_code).exists():
                rereceiver_is_valid = True
                receiver_exists = User_code.objects.filter(username_code=receiver_code).first()
            
            if SendToken.objects.filter(token=user_token).exists():

                if SendToken.objects.filter(token=user_token, user_token=user_exists).exists():
                    token_sneder = True
            

            ## send message
            if sender_is_valid and rereceiver_is_valid and token_sneder:
                message = Messages(message_text=message_text, sender_user=user_exists, receiver_user=receiver_exists)
                message.save()

                return Response({"description":"Message successfully sended"}, status=status.HTTP_200_OK)

    
        except Exception as ex:
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        
        return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
    

class GetLastMessage(APIView):
    '''
    get user last message
    '''
    def post(self, request, foramt=None):
        try:
            user_code = request.data["user_code"]
            user_token = request.data["user_token"]

            sender_is_valid = False

            if User_code.objects.filter(username_code=user_code).exists():

                sender_is_valid = True
                user_exists = User_code.objects.filter(username_code=user_code).first()

            if SendToken.objects.filter(token=user_token).exists():

                if SendToken.objects.filter(token=user_token, user_token=user_exists).exists():
                    token_sneder = True           
                
            if sender_is_valid and token_sneder:

                last_message = Messages.objects.filter(receiver_user=user_exists).last()
                serializer = MessagesSerializer(last_message)
                
                return Response(serializer.data, status=status.HTTP_200_OK)


            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
 

class UpadteUserCode(APIView):
    '''
    update user code
    '''
    def post(self, request, format=None):
        try:
            user_code = request.data["user_code"]
            user_token = request.data["user_token"]

            user_valid = False
            token_valid = False
            if User_code.objects.filter(username_code=user_code).exists():
                user_valid = True
                user_exists = User_code.objects.filter(username_code=user_code).first()

            if SendToken.objects.filter(token=user_token).exists():

                if SendToken.objects.filter(token=user_token, user_token=user_exists).exists():
                    token_valid = True   

            if user_valid and token_valid:        
                user_new_code = User_code.objects.filter(username_code=user_code).first()
                new_code = UserCodeCreator()
                user_new_code.username_code = new_code
                user_new_code.save()
                return Response({"description":"User Code successfully Updated","user_code":new_code}, status=status.HTTP_200_OK)

            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as ex:
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        
    

class UpadteToken(APIView):
    '''
    update user token
    '''
    def post(self, request, format=None):
        try:
            user_code = request.data["user_code"]
            user_token = request.data["user_token"]

            user_valid = False
            token_valid = False
            if User_code.objects.filter(username_code=user_code).exists():
                user_valid = True
                user_exists = User_code.objects.filter(username_code=user_code).first()

            if SendToken.objects.filter(token=user_token).exists():

                if SendToken.objects.filter(token=user_token, user_token=user_exists).exists():
                    token_valid = True

            if user_valid and token_valid:
                user_new_token = SendToken.objects.filter(token=user_token, user_token=user_exists).first()
                new_token = TokenCreator()
                user_new_token.token = new_token
                user_new_token.save()
                return Response({"description":"User Token successfully Updated","new_token":new_token}, status=status.HTTP_200_OK)

            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as ex:
            return Response({"description":"Input is incorrect"}, status=status.HTTP_400_BAD_REQUEST)