from django.db import models
from django.conf import settings

from realtyna.utils.models import BaseModel


class ListingOwner(BaseModel):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Room(BaseModel):
    owned_by = models.ForeignKey(
        ListingOwner,
        on_delete=models.CASCADE,
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