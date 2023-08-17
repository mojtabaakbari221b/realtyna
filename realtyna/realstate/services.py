from datetime import datetime

from .models import Reservation, Room


def room_reservation_create(*, room: Room, booked_by: str, reserved_until: datetime) -> Reservation:
    return Reservation.objects.create(
        room=room,
        booked_by=booked_by,
        reserved_until=reserved_until,
    )