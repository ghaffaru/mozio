from django.urls import path
from . import views

urlpatterns = [
    path('provider', views.ProviderListCreateView.as_view()),
    path('provider/<int:id>', views.ProviderRetrieveUpdateDeleteView.as_view()),

    path('polygon', views.PolygonListCreateView.as_view()),
    path('polygon/<int:id>', views.PolygonRetrieveUpdateDeleteView.as_view()),

    path('polygons-for-provider/<int:provider_id>', views.PolygonsForProviderView.as_view()),
    path('filter-polygons/<lat>/<long>', views.FilterPolygonsView.as_view())
]
