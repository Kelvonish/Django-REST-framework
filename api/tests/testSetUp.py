from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from api.models import Customer,Order



class TestSetUp(APITestCase):

    def setUp(self):
        self.create_customer_url = reverse('customer-list')
        self.create_order_url = reverse('order-list')
        self.fake = Faker()

        self.customer_data = {
            'name': "test two",
            'email': self.fake.email(),
            'phone': 254712345678,
        }
        self.order_data = {
            'item': self.fake.email().split('@')[0],
            'amount': 20000,
            'customer': "http://127.0.0.1:8000/customerApi/1/",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()