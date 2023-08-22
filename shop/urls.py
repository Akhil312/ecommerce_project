from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.allprodcat, name="allprodcat"),
    path('<slug:c_slug>/', views.allprodcat, name="prod_by_cat"),
    path('<slug:c_slug>/<slug:p_slug>/',views.proddetail,name="prodcatdetail"),
]

