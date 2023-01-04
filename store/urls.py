from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsView,name='collections-view'),
    path('collections/<str:cat_slug>/<str:pro_slug>',views.productDetails,name='product-details'),
]

