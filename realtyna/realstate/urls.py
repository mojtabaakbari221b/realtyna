from rest_framework.routers import DefaultRouter

from .api import viewsets


router = DefaultRouter()

router.register(r'hotel', viewsets.HotelViewset, basename='hotel')
router.register(r'hotel/(?P<hotel_id>[\w-]+)/room', viewsets.RoomViewset, basename='room')

urlpatterns = router.urls