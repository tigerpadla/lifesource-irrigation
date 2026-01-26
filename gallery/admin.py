from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectCategory, ProjectImage


class ProjectImageInline(admin.TabularInline):
    """Inline admin for adding multiple images to a project"""
    model = ProjectImage
    extra = 3  # Show 3 empty slots by default
    fields = ['image', 'caption', 'order', 'image_preview']
    readonly_fields = ['image_preview']
    ordering = ['order', 'id']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 120px; object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'get_categories', 'location', 'image_count', 'featured', 'created_at']
    list_filter = ['categories', 'featured']
    list_editable = ['featured']
    search_fields = ['title', 'description', 'location']
    filter_horizontal = ['categories']
    inlines = [ProjectImageInline]
    
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description')
        }),
        ('Details', {
            'fields': ('categories', 'location', 'featured')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 80px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Cover"
    
    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'
    
    def image_count(self, obj):
        count = obj.image_count
        if count > 1:
            return format_html('<span style="color: green; font-weight: bold;">{} images</span>', count)
        return "1 image"
    image_count.short_description = 'Images'
