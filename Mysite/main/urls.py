from django.urls import path
from .views import HelloListAndFormView

urlpatterns = [
    path('', HelloListAndFormView.as_view(), name='main')
]