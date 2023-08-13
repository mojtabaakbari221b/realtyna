from django.contrib import admin

from . import models


@admin.register(models.ListingOwner)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
    )


@admin.register(models.Room)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "owned_by",
    )


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "booked_by",
        "reserved_until",
    )
