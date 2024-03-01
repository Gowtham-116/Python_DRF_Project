from django.urls import path
from . import views

urlpatterns = [
    path("",views.review),
    path("thank_you", views.ThankyouView.as_view()),
    path("reviews",views.Reviewlistview.as_view())
]