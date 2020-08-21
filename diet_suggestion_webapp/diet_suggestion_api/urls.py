from django.urls import path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('predict_food_item/', views.PredictFoodItem.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
