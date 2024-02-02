from django.test import TestCase
from products.models import ProductModel
from django.utils import timezone
# Create your tests here.
print('############ Test Model')
class ProductModel_Test(TestCase):
    def test_pro_model(self):
        print('### inside test_pro_model')
        pname='fan'
        price=12000
        stock=5
        created_at=timezone.now()
        updated_at=timezone.now()
        p_model=ProductModel.objects.create(pname=pname,
            price=price,stock=stock,created_at=created_at,updated_at=updated_at)

        self.assertEqual(p_model.pname,pname),
        self.assertEqual(p_model.price,price)
        self.assertEqual(p_model.stock,stock)
        self.assertTrue(p_model.created_at,created_at)
        self.assertTrue(p_model.updated_at,updated_at)


