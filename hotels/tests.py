from django.test import TestCase

# def add(a, b):
#     return a+b
#
# class SalesTest(TestCase):
#     def test_add(self):
#         result = add(2, 4)
#         self.assertEqual(result, 6)
#         result = add(1, 2)
#         self.assertEqual(result, 3)
#
#     def test_two(self):
#         self.assertEqual(5, 5)
from django.urls import reverse
from django.contrib.auth.models import User
# в тестах отдельно создается база данных, только для тестов
from rest_framework import status

from hotels.models import Hotels


class SalesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('usernamee')  # создаем юзера
          # залогинили клиента под юзером

    def test_create_hotel(self):
        self.client.force_login(self.user)
        url = reverse('create-hotel')  # получает имя эндпоинта(урла) и возвращает урл
        data = {
            "name": "tests_na",
            "city": "test_city",
            "picture": open('/home/mkl/7.jpg', 'rb')
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(response.data['name'], data['name'])  # проверяем, что текст который мы записали и нам \
        # вернул сервер, совпадают
        hotel = Hotels.objects.get(**data)
        self.assertEqual(response.data['id'], hotel.id)