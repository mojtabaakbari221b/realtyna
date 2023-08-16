from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from django.utils.timezone import now

from .models import Reservation
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


def specific_hotel_room_with_prefetched_reservation_list(*, user: User, hotel_id: int):
    return specific_hotel_room_list(
        user=user,
        hotel_id=hotel_id,
    ).prefetch_related(
        Prefetch(
            'reservation_set',
            queryset=Reservation.objects.filter(
                reserved_until__gt=now(),
            ),
        ),
    )
