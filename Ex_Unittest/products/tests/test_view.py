from django.test import Client,TestCase
from products import views
from products.models import ProductModel
import json
print('############ Test View')
class ProductsAllView_Test(TestCase):
    def test_showprod(self): # folder name should be test_ and fun name must be start with test_
        print('### inside test_showprod')
        ProductModel.objects.create(
            pname= "fan",
            price= "3.00",
            stock= 3500,
            created_at= "2024-02-02T11:02:51.737Z",
            updated_at= "2024-02-02T11:02:51.737Z"
            )
        ProductModel.objects.create(
            pname= "washing machine",
            price= "20000.00",
            stock= 3,
            created_at= "2024-02-02T11:04:45.784Z",
            updated_at= "2024-02-02T11:04:45.784Z"
        )
        
    def show_test_view(self,Client):
        client = Client()
        response=client.get("/prod/")
        self.assertEqual(response.status_code,200)
    
        expected_output={
            "products": [
            {
            "id": 2,
            "pname": "fan",
            "price": "3.00",
            "stock": 3500,
            "created_at": "2024-02-02T11:02:51.737Z",
            "updated_at": "2024-02-02T11:02:51.737Z"
            },
            {
            "id": 3,
            "pname": "washing machine",
            "price": "20000.00",
            "stock": 3,
            "created_at": "2024-02-02T11:04:45.784Z",
            "updated_at": "2024-02-02T11:04:45.784Z"
            }
        ]}
        self.assertEqual(json.load(response.content),expected_output)