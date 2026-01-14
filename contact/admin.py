from django.contrib import admin
from .models import ContactInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'is_contacted', 'created_at']
    list_filter = ['is_contacted', 'referral_source', 'created_at']
    list_editable = ['is_contacted']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('services_needed', 'referral_source', 'message')
        }),
        ('Status', {
            'fields': ('is_contacted', 'notes', 'created_at')
        }),
    )
