# Django-REST-framework
It contains API endpoint to create, retrieve, update and delete customers with their respective orders.

DjangoCustomerOrderApi
CustomerApi
This deals with the customer model in the database. It is used to create, delete, update and retrievecustomer details
GET List Customers
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/
HEADERS
Authorization
Example Request List Customers
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/"
payload headers == {{}
(^) } 'Authorization': ''
(^) response=requests.request("GET",url,headers=headers View More ,data=payload)
Documentation Settings

POST Create Customer
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/
HEADERS
BODY formdata
Authorization
name
Name of the customer which should be a string
email
email of the customer
phone
Please use 254712345678 format
Example Request Create Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/"
payload 'email':= ''{'name', : '',
'phone'files =: ['' }
(^) ]

PUT Update Customer
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/
View More
Documentation Settings
HEADERS
BODY formdata
Authorization
name
name of the customer
email email of the customer
phone
phone of the customer. It should follow 254712345678
Example Request Update Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/"
payload = {'name': '','email': '',
'phone': ''}files = [
(^) ]

DEL Delete Customer
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/
HEADERS
PARAMS
Authorization
View More
Documentation Settings
BODY formdata
customer_id
This is the id of the customer to be deleted in the database
Example Request Delete Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/"
payload = {'customer_id': ''}files = [
]headers = { (^)
(^) 'Authorization':''

GET Single Customer details
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/
HEADERS
BODY formdata
Authorization
customer_id This the the id of the customer in the database
Example Request Single Customer details
View More
Documentation Settings
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/"
payload = {'customer_id': ''}files = [
]headers = { (^)
(^) 'Authorization':''

OrderApi
This deals with the order model in the database. It is used to create, delete, update and retrieve orderdetails
GET List Orders
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/
HEADERS
Authorization
Example Request List Orders
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/"
payload = {}headers = {
'Authorization': ''}
(^) response= requests.request("GET",url,headers=headers,data= payload)

View More
View More
Documentation Settings
POST Create Order
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/
HEADERS
BODY formdata
Authorization
item
This is the name of the item
amount
This is the amount of the item
customer
Url to the customer
Example Request Create Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/"
payload = {'item': '','amount': '',
'customer': ''}files = [
(^) ]

PUT Update Order
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/
View More
Documentation Settings
HEADERS
BODY formdata
Authorization
customer_id 2
order_id This is the id of the order in the databse to be updated
item
This is the name of the item
amount the cost of the item
customer
Url to the customer
Example Request Update Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/"
payload = {'order_id': '','item': '',
'amount': '','customer': ''} (^)
files = [^

DEL Delete Order
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/
View More
Documentation Settings
HEADERS
BODY formdata
Authorization
order_id This is the id of the order in the databse to be deleted
Example Request Delete Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/"
payload = {'order_id': ''}files = [
]headers = { (^)
(^) 'Authorization':''

GET Single Order details
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/
BODY formdata
order_id
This is the id of the order in the databse to be fetched
