# from django.urls import path,include
# from watchlist_app.api.views import movielist,movie_detail

# urlpatterns = [
#     path('list/',movielist,name='movie-list'),
#     path('<int:pk>',movie_detail,name='movie-detail')
# ]
from django.urls import path,include
# from watchlist_app.views import movielist,movie_detail
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import MoviedetailAV,MovielistAV,StreamplatformVS,Reviewlist,ReviewDetail,Reviewcreate #,StreamingAV,StreamdetailAV

router=DefaultRouter()
router.register('stream',StreamplatformVS,basename='streamplatform')
urlpatterns = [
    path('list/',MovielistAV.as_view(),name='movie-list'),
    path('<int:pk>/',MoviedetailAV.as_view(),name='movie-detail'),
    
    path('',include(router.urls)),
    
    # path('stream/',StreamingAV.as_view(),name='StreamingAV'),
    # path('stream/<int:pk>',StreamdetailAV.as_view(),name='streamplatform-detail'),
    
    path('<int:pk>/review-create/',Reviewcreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',Reviewlist.as_view(),name='review-list'),
    path('review/',Reviewlist.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail') 
]
 