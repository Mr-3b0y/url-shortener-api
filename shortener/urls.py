from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShortenViewset, RedirectView

router = DefaultRouter()
router.register('shorten', ShortenViewset, basename='shorten-actions')


urlpatterns = [
    path('', include(router.urls)),
    path('<str:short_code>/', RedirectView.as_view({'get': 'retrieve'}), name='shorten-redirect')
]

