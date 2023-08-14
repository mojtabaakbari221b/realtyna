from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


def non_reserved_room_for_specific_hotel_list(*, hotel_id: int):
    return models.Room.objects.filter(
        is_reserved=False,
        hotel__id=hotel_id,
    )


def specific_user_hotel_list(*, user: User):
    return models.Hotel.objects.filter(
        hotelier=user,
    )


def specific_hotel_room_list(*, user: User, hotel_id: int):
    return models.Room.objects.filter(
        hotel_id=hotel_id,
        hotel__hotelier=user,
    )