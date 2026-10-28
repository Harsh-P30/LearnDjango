from django.urls import path
from .views import singleobj,multipleobj,MultipleObjView

urlpatterns = [
    path('singleobj/<int:id>/',singleobj),
    path('multipleobj/',multipleobj),
    path('multipleobjview/',MultipleObjView.as_view())
]


# concreate classes,genericapiview