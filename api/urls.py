from django.urls import path
from api.views.user import UserView
from api.views.car import CarApiView
from api.views.car_update import CarUpdateApiView

urlpatterns = [
    path('token', UserView.as_view()),
    path('car', CarApiView.as_view()),
    path('car/<int:pk>', CarUpdateApiView.as_view()),
]