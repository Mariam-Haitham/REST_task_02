
from django.contrib import admin
from django.urls import path
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', views.FlightsList.as_view(), name="flights-list"),
    path('bookings/', views.BookingsList.as_view(), name="bookings-list"), 
    path('bookings/<int:Booking_id>', views.BookingDetail .as_view(), name="booking-details"),
    path('bookings/<int:Booking_id>/update', views.BookingUpdate .as_view(), name="update-booking"),
    path('bookings/<int:Booking_id>/delete', views.BookingDelete .as_view(), name="cancel-booking"), 
]
