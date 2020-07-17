from django.urls import path, include
from . import views


from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('first', views.first),             # можно удалить, низкоуровневый пробник
    # path('another', Another.as_view()),     # можно удалить, низкоуровневый пробник
    path('', include(router.urls)),
]
