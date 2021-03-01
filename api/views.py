from django.shortcuts import render
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import customerSerializer,orderSerializer
from .models import Customer, Order
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import africastalking
import requests
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.


@api_view(['GET'])
def listUsers(request):
    users = Customer.objects.all()
    serializedData = customerSerializer(users, many=True)

    return Response(serializedData.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createUser(request):
    serializedData = customerSerializer(data=request.data)

    if serializedData.is_valid():
        serializedData.save()
        return Response(serializedData.data, status=201)

    return Response(serializedData.errors, status=400)


@api_view(['GET', 'PUT'])
def detailUser(request, pk):

    try:
        snippet = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = customerSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = customerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteuser(request, pk):
    try:
        snippet = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ordersApi(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Order.objects.all()
    serializer_class = orderSerializer 

    def create(self, request):
        serializer_context = {
            'request': request,
        }
        serializedData = orderSerializer(data=request.data,context=serializer_context)
       
        if serializedData.is_valid():
            

            if serializedData.save():
                usernameApi = "djangoapi"
                password = "djangoapi"
                res = requests.get(request.data['customer'],auth=(usernameApi,password))
                print(res)
                resJson = res.json()
                phoneInt = resJson['phone']
                print(phoneInt)
                phone = str(phoneInt)

                print(phone)
            # Initialize SDK
                username = "janetmomanyi"    # use 'sandbox' for development in the test environment
                api_key = "f47d76ff6cb911d5f290e29e69d0cd17c199123faf67b31d3c91555fc9569b53"      # use your sandbox app API key for development in the test environment
                africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
                sms = africastalking.SMS


# Use the service synchronously
                response = sms.send("Order is added from django rest api for product "+request.data['item']+ " amount is "+request.data['amount'], ["+"+phone])
                print(response)

# Or use it asynchronously
                def on_finish(error, response):
                    if error is not None:
                        raise error
                    print(response)

                    sms.send("Hello django rest api", ["+254706783609"], callback=on_finish) 

                return Response(serializedData.data, status=201)

        return Response(serializedData.errors, status=400)


class customerApi(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Customer.objects.all()
    serializer_class = customerSerializer

    



#orders

def listOrders(request):
    users= Order.objects.all()
    serializedData = customerSerializer(users,many=True)
    
    return Response(serializedData.data,status=status.HTTP_200_OK)


def Login(request):
    token=""
    if request.user.id == None:
        print('none')
    else:
        userActive = User.objects.get(username=request.user)   
        token,created= Token.objects.get_or_create(user=userActive)
        print(token)
        print(created)
        '''if token==None:
            token = Token.objects.create(user=userActive)
            print(token.key)
            #obj = Token.objects.get(user = request.user)'''
    context={
        "userActive":token
    }
    return render(request,'test.html',context) 

    
def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.
    



    
