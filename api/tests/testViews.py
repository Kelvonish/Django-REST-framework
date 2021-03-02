from .testSetUp import TestSetUp
from api.models import Order,Customer


class TestViews(TestSetUp):
    def test_user_cannot_create_customer_with_no_data(self):
        res = self.client.post(self.create_customer_url2)
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_create_customer_with_no_token(self):
        res = self.client.post(self.create_customer_url)
        self.assertEqual(res.status_code, 401)


    def test_user_cannot_create_order_with_no_token(self):
        res = self.client.post(self.create_order_url)
        self.assertEqual(res.status_code, 401)

    def test_user_cannot_create_order_with_no_data(self):
        res = self.client.post(self.create_customer_url2)
        self.assertEqual(res.status_code, 400)

    