from datetime import timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now
from rest_framework.test import APITestCase
from model_bakery import baker


class TestMixin :
    _USER_EMAIL = "realtyna@realstate.com"
    _USER_PASSWORD = "realtyna"

    def setUp(self): #NOSONAR
        self.user = baker.make(
            get_user_model(),
            email=self._USER_EMAIL,
            password=self._USER_PASSWORD,
        )

        self.client.force_authenticate(user=self.user)


class TestRoomReservation(TestMixin, APITestCase):
    def setUp(self):
        super().setUp()

        self.room = baker.make(
            'realstate.room',
            hotel__hotelier=self.user,
        )

        self.url = reverse(
            'room-reserve',
            args=(
                self.room.hotel.id,
                self.room.id,
            ),
        )


    def test_reserve(self):
        data = {
            "booked_by" : "realtyna",
            "reserved_until" : now(),
        }   
        
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 204)

    def test_reserve_reserved_room(self):
        future_date_after_2days = now() + timedelta(days = 2)

        data = {
            "booked_by" : "realtyna",
            "reserved_until" : future_date_after_2days,
        }

        self.client.post(self.url, data=data)
        
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 403)

        