from django.db.migrations import serializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import (
    viewsets,
    status,
    generics as gen
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .my_mixin import CountViewMixin
from .models import News, Viewer
from .serializers import NewsSerializer


class NewsModelViewSet(CountViewMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_news_instance(self, pk):
        return gen.get_object_or_404(self.queryset, pk=pk)

    @swagger_auto_schema(
        method="get",
        operation_description="Получает список всех новостей.",
        operation_summary="Получение списка всех новостей",
        operation_id="list_news",
        tags=["Новости"],
        responses={
            200: openapi.Response(description="OK - Список новостей получен успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
        },
    )
    @action(detail=True, methods=['get'])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method="get",
        operation_description="Получает конкретную новость по ее идентификатору.",
        operation_summary="Получение конкретной новости",
        operation_id="retrieve_news",
        tags=["Новости"],
        responses={
            200: openapi.Response(description="OK - Новость получена успешно."),
            401: openapi.Response(description="Ошибка аутентификации"),
            404: openapi.Response(description="Not Found - Новость не найдена"),
        },
    )
    @action(detail=True, methods=['get'])
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_news_instance(kwargs['pk'])
        except News.DoesNotExist:
            return Response(
                {
                    "detail": "Новость не найдена."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        # serializer = self.get_serializer(instance)
        ip = self.get_client_ip(request)
        if Viewer.objects.filter(ipaddress=ip).exists():
            # instance.viewers += 1
            instance.save()
        else:
            Viewer.objects.create(ipaddress=ip)
            # instance.viewers += 1

        serializer = NewsSerializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        method="put",
        operation_description="Обновляет информацию о существующей новости.",
        operation_summary="Обновление новости",
        operation_id="update_news",
        tags=["Новости"],
        responses={
            200: openapi.Response(description="OK - Новость обновлена успешно."),
            400: openapi.Response(description="Bad Request - Некорректный запрос"),
        },
    )
    @action(detail=True, methods=['put'])
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        method="post",
        operation_description="Создает новую новость.",
        operation_summary="Создание новости",
        operation_id="create_news",
        tags=["Новости"],
        request_body=NewsSerializer,
        responses={
            201: openapi.Response(description="Created - Новость успешно создана."),
            400: openapi.Response(description="Bad Request - Некорректный запрос"),
        },
    )
    @action(detail=False, methods=['post'])
    def create(self, request):
        news_instance = self.get_serializer(data=request.data)
        if news_instance.is_valid():
            news_instance.save()
            return Response(
                news_instance.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            news_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        method="delete",
        operation_description="Удаляет существующую новость.",
        operation_summary="Удаление новости",
        operation_id="delete_news",
        tags=["Новости"],
        responses={
            204: openapi.Response(description="No Content - Новость успешно удалена."),
            404: openapi.Response(description="Not Found - Новость не найдена"),
        },
    )
    @action(detail=False, methods=['delete'])
    def destroy(self, request, pk=None):
        try:
            instance = self.get_news_instance(pk)
            instance.delete()
            return Response(
                {
                    "detail": "Новость успешно удалена."
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except News.DoesNotExist:
            return Response(
                {
                    "detail": "Новость не найдена."
                },
                status=status.HTTP_404_NOT_FOUND
            )






