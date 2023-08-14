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

    is_reserved = models.BooleanField(
        default=False,
    )


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