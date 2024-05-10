from django.contrib import admin
from .models import (
    News,
    Tag,
    Viewer
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'text',
        'image',
        # 'tags',
        # 'viewers',
        'created_at',

    )
    ordering = ('title',)
    filter_horizontal = ('tags',)  # Используем filter_horizontal для выбора нескольких значений

    # def get_prepopulated_fields(self, request, obj=None):   # autofill in admin
    #     return {
    #         'tags': ('tags',),
    #     }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_filter = (
        'name',
    )
    ordering = ('name',)

    # def get_prepopulated_fields(self, request, obj=None):
    #     return {
    #         'slug': ('title',),
    #     }


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ipaddress',
    )

