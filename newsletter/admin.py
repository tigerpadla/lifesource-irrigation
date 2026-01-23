from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
from .models import Newsletter, Subscriber, Testimonial


@admin.register(Newsletter)
class NewsletterAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title', 'is_published', 'published_at', 'created_at']
    list_filter = ['is_published', 'published_at']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'excerpt', 'content', 'image')
        }),
        ('Irish Corner', {
            'fields': ('irish_fact',),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.is_published and not obj.published_at:
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    list_editable = ['is_active']
    search_fields = ['email']
    date_hierarchy = 'subscribed_at'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'location', 'project_type', 'is_active', 'created_at']
    list_filter = ['is_active', 'project_type']
    list_editable = ['is_active']
    search_fields = ['client_name', 'quote', 'location']
