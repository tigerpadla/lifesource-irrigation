from django.contrib import admin
from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_categories', 'location', 'featured', 'created_at']
    list_filter = ['categories', 'featured']
    list_editable = ['featured']
    search_fields = ['title', 'description', 'location']
    filter_horizontal = ['categories']  # Nice dual-list widget for selecting multiple categories
    
    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'
