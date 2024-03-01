from django.urls import path
from . import views
urlpatterns=[
    #path('january', views.jan),
#---if a req path reaches /january execute jan view function, this is an urlconfig
    #path('february', views.feb)
    path('',views.index, name='index'), #/challenges/
    path('<int:month>',views.mon_chal_bynum),
    path('<str:month>',views.monthly_challenge,name='monthly_challenge')
]
 