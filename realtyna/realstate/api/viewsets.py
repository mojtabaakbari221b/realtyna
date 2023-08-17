from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from ..selectors import (
    specific_user_hotel_list,
    specific_hotel_room_with_prefetched_reservation_list,
    specific_hotel_available_room_in_preferred_time_list,
)
from ..services import room_reservation_create
from .serializers import (
    HotelSerializer,
    RoomSerializer,
    ReservationSerializer,
    RoomAvailabilitySerializer,
)
from .permissions import CheckRoomIsNotReserved


class HotelViewset(ModelViewSet):
    serializer_class = HotelSerializer

    def get_queryset(self):
        return specific_user_hotel_list(
            user=self.request.user,
        )
    
    @action(
        methods=[
            "get",
        ],
        renderer_classes = [
            TemplateHTMLRenderer,
        ],
        detail=True,
    )
    def overview(self, request, pk):
        hotel_rooms = specific_hotel_room_with_prefetched_reservation_list(
            user=request.user,
            hotel_id=pk,
        )
        content = {
            "hotel_rooms" : hotel_rooms,
        }
        return Response(
            content,
            template_name="realtyna/room_overview.html",
        )
    
    @action(
        methods=[
            "get",
        ],
        detail=True,
    )
    def room_availability_status(self, request, pk):
        serializer = RoomAvailabilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        available_room_count = specific_hotel_available_room_in_preferred_time_list(
            hotel_id=pk,
            preferred_time=serializer.validated_data.get("preferred_time"),
        ).count()

        requested_room = serializer.validated_data.get("requested_room_number")

        return Response(
            data={
                "available_room" : available_room_count,
                "requested_room" : requested_room,
                "is_requested_room_availabled" : available_room_count >= requested_room,
            },
        )


class RoomViewset(ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return specific_hotel_room_with_prefetched_reservation_list(
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
            "post",
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