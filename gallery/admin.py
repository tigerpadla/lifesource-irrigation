from django.contrib import admin
from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'featured', 'created_at']
    list_filter = ['category', 'featured']
    list_editable = ['featured']
    search_fields = ['title', 'description', 'location']
