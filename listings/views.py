from rest_framework import viewsets
from .models import Listing, Booking, Review, User
from .serializers import (
    ListingSerializer, BookingSerializer, ReviewSerializer, UserSerializer
)

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

