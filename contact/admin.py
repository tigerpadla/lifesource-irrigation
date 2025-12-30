from django.contrib import admin
from .models import ContactInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'property_type', 'is_contacted', 'created_at']
    list_filter = ['is_contacted', 'property_type', 'referral_source', 'created_at']
    list_editable = ['is_contacted']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'address']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Property Details', {
            'fields': ('address', 'property_type')
        }),
        ('Inquiry Details', {
            'fields': ('services_needed', 'referral_source', 'message')
        }),
        ('Status', {
            'fields': ('is_contacted', 'notes', 'created_at')
        }),
    )
