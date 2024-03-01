from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.StartingpageView.as_view(),name='starting-page'),
    path('posts',views.AllpostsView.as_view(),name='post-page'),
    path('posts/<slug:slug>',views.PostdetailView.as_view(),name='detail-post-page')#pathconvertor:pathname
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
