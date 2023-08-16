from django.db import models
from django.conf import settings

from realtyna.utils.models import BaseModel


class Hotel(BaseModel):
    name = models.CharField(
        max_length=256,
    )
    
    hotelier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Room(BaseModel):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
    )

    room_number = models.PositiveSmallIntegerField(
        default=0,
    )

    @property
    def is_reserved(self):
        return self.reservation_set.exists()
    
    @property
    def reserved_until(self):
        if not self.is_reserved :
            return "Not reserved"
        
        max_id = 0
        max_object = None

        for reservation in self.reservation_set.all():
            if reservation.id > max_id :
                max_id = reservation.id
                max_object = reservation

        return max_object.reserved_until


class Reservation(BaseModel):
    room = models.ForeignKey(
        Room,
        null=True,
        on_delete=models.SET_NULL,
    )

    booked_by = models.CharField(
        max_length=256,
    )
    
    reserved_until = models.DateTimeField()