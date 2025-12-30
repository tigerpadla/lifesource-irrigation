from django.contrib import admin
from .models import ServiceCategory, SubService


class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 1


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order', 'is_active', 'updated_at']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SubServiceInline]


@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']
