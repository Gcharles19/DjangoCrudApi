from django.urls import path, include
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]