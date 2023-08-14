from rest_framework import serializers

from .. import models
from ..selectors import non_reserved_room_for_specific_hotel_list


class HotelSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict):
        request = self.context.get("request")

        validated_data.update(
            {
                "hotelier" : request.user,
            },
        )

        return super().create(validated_data)
    
    class Meta:
        model = models.Hotel
        fields = [
            "id",
            "name",
        ]


class RoomSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict):
        hotel_id = self.context.get("hotel_id")

        validated_data.update(
            {
                "hotel_id" : hotel_id,
            },
        )

        return super().create(validated_data)
    
    class Meta:
        model = models.Room
        fields = [
            "id",
            "room_number",
            "is_reserved",
        ]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = [
            "id",
            "booked_by",
            "reserved_until",
        ]