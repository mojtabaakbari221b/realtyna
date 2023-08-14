from django.contrib import admin

from . import models


@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "hotelier",
    )


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "hotel",
    )


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "booked_by",
        "reserved_until",
    )
