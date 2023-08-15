from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView

from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()

class MenuViewTest(TestCase):

    # def __init__(self):
    #     carte = None

    carte = [ 
                ['Bruschetta', 4.50, 27, ],
                ['Lamb rib', 17.30, 20, ],
                ['Pork rib', 16.75, 30, ] ,
                ['Corn pudim', 5.40, 50 ] ,
                ['Calamari salad', 8.25, 23], 
    ]

    def setUp(self):
        [ Menu.objects.create(title=dish[0], price=dish[1], inventory=dish[2]) for dish in MenuViewTest.carte ]

    def test_get_item(self):
        item_id = 2
        i = int(item_id) - 1
        d = MenuViewTest.carte
        url = reverse('singlemenuview', args = [item_id])
#        url = reverse('singlemenuview',args = [3])
#        url = reverse('singlemenuview',args = [3])
#        url = '/restaurant/menu/3'
        print("URL: ", url)
        response = client.get(url)
#        response = client.get(reverse('singlemenuview', args = [item_id]))
        print(response.status_code)
        print(response.data)
        item = { 'id' : i, 'title': d[i][0], 'price': d[i][1], 'inventory': d[i][2] }
#        self.assertDictEqual(response.data,MenuViewTest.carte[1])
        self.assertDictEqual(response.data,item)

    def test_get_all(self):
        url = reverse('menuview')
        print(url)

        response = client.get(url)
#        response = client.get(reverse('menuview'))
        print(response.data)
        print(response.status_code)
        self.assertEqual(len(response.data), len(MenuViewTest.carte))
#        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

