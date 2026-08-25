from django.urls import path
from .views import singleobj,multipleobj

urlpatterns = [
    path('singleobj/<int:id>/',singleobj),
    path('multipleobj/',multipleobj)
]
