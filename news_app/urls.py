from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import NewsModelViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        # News
        path("news/", NewsModelViewSet.as_view({"get": "list"}), name="news-list"),
        path("news/create/", NewsModelViewSet.as_view({"post": "create"}), name="news-create"),
        path("news/<int:pk>/", NewsModelViewSet.as_view({"get": "retrieve"}), name="news-retrieve"),
        path("news/<int:pk>/update/", NewsModelViewSet.as_view({"put": "update"}), name="news-update"),
        path("news/<int:pk>/delete/", NewsModelViewSet.as_view({"delete": "destroy"}), name="news-delete"),
    ]
)
