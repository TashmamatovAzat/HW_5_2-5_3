from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('item/<int:item_id>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),

    path('firm/', views.FirmListCreateAPIView.as_view()),
    path('firm/<int:firm_id>/', views.FirmRetrieveUpdateDestroyAPIView.as_view()),

    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:category_id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
]