from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ..selectors import (
    specific_user_hotel_list,
    specific_hotel_room_list,
)
from ..services import room_reservation_create
from .serializers import (
    HotelSerializer,
    RoomSerializer,
    ReservationSerializer,
)
from .permissions import CheckRoomIsNotReserved


class HotelViewset(ModelViewSet):
    serializer_class = HotelSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return specific_user_hotel_list(
            user=self.request.user,
        )
    

class RoomViewset(ModelViewSet):
    serializer_class = RoomSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return specific_hotel_room_list(
            user=self.request.user,
            hotel_id=self.kwargs.get("hotel_id"),
        )
    
    def get_permissions(self):
        permissions = super().get_permissions()

        if self.action == "reserve" :
            permissions.append(CheckRoomIsNotReserved())

        return permissions
    
    def get_serializer_context(self, **kwargs):
        context = super().get_serializer_context()
        context["hotel_id"] = self.kwargs.get("hotel_id")
        return context
    
    @action(
        methods=[
            "get",
        ],
        detail=True,
    )
    def reserve(self, request, hotel_id, pk):
        room = self.get_object()

        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        room_reservation_create(
            room=room,
            reserved_until=serializer.validated_data.get("reserved_until"),
            booked_by=serializer.validated_data.get("booked_by"),
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )