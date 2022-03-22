from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProviderListCreateView.as_view()),
    path('<int:id>', views.ProviderRetrieveUpdateDeleteView.as_view())
]