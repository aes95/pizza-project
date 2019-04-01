from django.test import *
from django.contrib.auth.models import User
from .models import *
# Create your tests here.

class ModelsTestCase(TestCase):
    def setUp(self):
        tops = ['Pepperoni', 'Sausage','Mushrooms','Onions','Ham','Canadian Bacon','Pineapple','Eggplant','Tomato & Basil','Green Peppers','Hamburger','Spinach','Artichoke','Buffalo Chicken','Barbecue Chicken','Anchovies','Black Olives','Fresh Garlic','Zucchini']
        for top in tops:
            Topping(name=top)
        large = Pizza.objects.create(large=True)
        small = Pizza.objects.create()
        large_s = Pizza.objects.create(large=True, sicilian=True)
        small_s = Pizza.objects.create(sicilian=True)
        PizzaPrice(sicilian=True, large=False, toppings_count=1)


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret@1'}
        user = User.objects.create_user(**self.credentials)
        user.save()

    def test_login(self):
        # send login data
        response = self.client.post('/login', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_failed_login(self): #try with wrong pwd
        response = self.client.post('/login', {'username': 'testuser','password': 'Secret@1'}, follow=True)
        self.assertEqual(response.status_code, 200)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_register(self):
        pass

    def test_logout(self):
        response = self.client.post('/login', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTrue(response.context['user'].is_active)
        #logout
        response = self.client.get('/logout',follow=True)
        self.assertFalse(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
