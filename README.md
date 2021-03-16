# Django-REST-framework
It contains API endpoint to create, retrieve, update and delete customers with their respective orders..

#For an extensive online documentation visit https://documenter.getpostman.com/view/5714554/TWDfCswS
link to the api service to generate your access token https://django-rest-customer-api.herokuapp.com/

# DjangoCustomerOrderApi

## CustomerApi

#### This deals with the customer model in the database. It is used to create, delete, update and retrieve customer details

### GET List Customers

```
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/
```
```
HEADERS
Authorization
```
```
Example Request List Customers

import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/"

payload = {}
headers = {
  'Authorization': ''
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```


### POST Create Customer

```
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/
```
```
HEADERS
```
```
BODY formdata
```
```
Authorization
```
```
name
Name of the customer which should be a string
email
email of the customer
phone
Please use 254712345678 format
```
```
Example Request Create Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/"
payload = {'name': '',
'email': '',
'phone': ''}
files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```

### PUT Update Customer

```
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/

```

```
HEADERS

```

```
BODY formdata
```

```
Authorization
```

```
name
name of the customer
email email of the customer
phone
phone of the customer. It should follow 254712345678
```

```
Example Request Update Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/2/"
payload = {'name': '',
'email': '',
'phone': ''}
files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("PUT", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```


### DEL Delete Customer

```
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/
```
```
HEADERS
```
```
PARAMS
```
```
Authorization
```



```
BODY formdata
customer_id
This is the id of the customer to be deleted in the database
```
```

Example Request Delete Customer
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/2/"

files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("DELETE", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```


### GET Single Customer details

```
https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/{{customer_id}}/
```
```
HEADERS
```
```
BODY formdata
```
```
Authorization
```
```
customer_id This the the id of the customer in the database
```
```
Example Request Single Customer details

url = "https://django-rest-customer-api.herokuapp.com/browsableApi/customerApi/1/"

payload = {}
files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```


```


## OrderApi

#### This deals with the order model in the database. It is used to create, delete, update and retrieve orderdetails

### GET List Orders

```
```
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/
```
```
HEADERS
Authorization
```
```
Example Request List Orders
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/"
payload = {}
headers = {
  'Authorization': ''
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```



### POST Create Order

```
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/
```
```
HEADERS
```
```
BODY formdata
```
```
Authorization
```
```
item
This is the name of the item
amount
This is the amount of the item
customer
Url to the customer
```
```
Example Request Create Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/"
payload = {'item': '',
'amount': '',
'customer': ''}
files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```
(^) ]

### PUT Update Order

```
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/1/
```


```
Documentation Settings
```

##### HEADERS

```
BODY formdata
```
```
Authorization
customer_id 2
```
```
order_id This is the id of the order in the databse to be updated
item
This is the name of the item
amount the cost of the item
customer
Url to the customer
```
```
Example Request Update Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/1/"
payload = {'order_id': '',
'item': '',
'amount': '',
'customer': ''}
files = [

]
headers = {
  'Authorization': '',
  'customer_id': '2'
}

response = requests.request("PUT", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```
### DEL Delete Order

```
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/
```


```
Documentation Settings
```

##### HEADERS

```
BODY formdata
```
```
Authorization
```
```
order_id This is the id of the order in the databse to be deleted
```
```
Example Request Delete Order
import requests
url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/2/"
payload = {}
files = [

]
headers = {
  'Authorization': ''
}

response = requests.request("DELETE", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```


### GET Single Order details

```
https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/
```
```
BODY formdata
order_id
This is the id of the order in the databse to be fetched

import requests

url = "https://django-rest-customer-api.herokuapp.com/browsableApi/orderApi/{{order_id}}/"

payload = {'order_id': ''}
files = [

]
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
```


