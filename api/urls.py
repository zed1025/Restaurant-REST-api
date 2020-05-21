from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('restaurants/', views.Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),
]
