from django.urls import path,include
# from watchlist_app.views import movielist,movie_detail
from watchlist_app.api.views import MoviedetailAV,MovielistAV


urlpatterns = [
    path('list/',MovielistAV.as_view(),name='movie-list'),
    path('<int:pk>',MoviedetailAV.as_view(),name='movie-detail')
]
 