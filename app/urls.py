from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('firm/', views.FirmListCreateAPIView.as_view()),
    path('category/', views.category_list_create_api_view),
]