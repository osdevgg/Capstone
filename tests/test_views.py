from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView

from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP
import time

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
        Menu.objects.raw('delete from test.restaurant_menu;')
        [ Menu.objects.create(title=dish[0], price=dish[1], inventory=dish[2]) for dish in MenuViewTest.carte ]


    def test_get_all(self):

        url = reverse('menuview')
#        print(url)

        # response = client.get(url)
        response = self.client.get(url)
#        response = client.get(reverse('menuview'))
        print(response.data)
#        print(response.status_code)
        self.assertEqual(len(response.data), len(MenuViewTest.carte))
#        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_aretrieve_item(self):

#        time.sleep(10) 
        item_id = 3
        i = item_id - 2
#       i = int(item_id)
        d = MenuViewTest.carte
        # url = reverse('singlemenuview', args = [item_id])
        url = reverse('singlemenuview', kwargs={'pk': item_id})
#        url = reverse('singlemenuview',args = [3])
#        url = reverse('singlemenuview',args = [3])
#        url = '/restaurant/menu/3'
#      #  print("URL: ", url)
        response = self.client.get(url)
#        response = client.get(reverse('singlemenuview', args = [item_id]))
#        print(response.status_code)
#        print(response.data)
#        item = { 'id' : i, 'title': d[i][0], 'price': d[i][1], 'inventory': d[i][2] }
#        price = round(d[i][1],2)
#        price = Decimal(round(d[i][1],2))
        price = Decimal(d[i][1])
        pricedec = price.quantize(Decimal('0.00'),rounding = ROUND_HALF_UP)
#        print(pricedec)
        item = { 'title': d[i][0], 'price': pricedec, 'inventory': d[i][2] }
#        item = { 'title': d[i][0], 'price': Decimal(d[i][1]), 'inventory': d[i][2] }
#        item = { 'title': d[i][0], 'inventory': d[i][2] }
#        self.assertDictEqual(response.data,MenuViewTest.carte[1])
        response_data = response.data.copy()
        response_data.pop('id', None)
#        response_data.pop('price', None)
#        self.assertDictEqual(response.data,item)
#        self.assertEqual(response.status_code,status.HTTP_200_OK)
#        self.assertDictEqual(response_data,item)
        self.assertDictEqual(OrderedDict(response_data),OrderedDict(item))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

