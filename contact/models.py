from django.db import models


class ContactInquiry(models.Model):
    """Contact form submissions"""
    SERVICE_CHOICES = [
        ('new_installation', 'Free Estimate - New Installation'),
        ('spring_startup', 'Spring Start-Up'),
        ('winterization', 'Winterization'),
        ('repair', 'Service & Repair'),
        ('maintenance', 'Maintenance Agreement'),
        ('lighting', 'Landscape Lighting'),
        ('assessment', 'System Assessment'),
        ('gardening', 'Gardening Services'),
        ('refurbishment', 'Terrace Refurbishment'),
        ('other', 'Other'),
    ]
    
    PROPERTY_CHOICES = [
        ('rooftop', 'Rooftop/Terrace'),
        ('penthouse', 'Penthouse'),
        ('townhouse', 'Townhouse/Backyard'),
        ('commercial', 'Commercial'),
        ('other', 'Other'),
    ]
    
    REFERRAL_CHOICES = [
        ('google', 'Google Search'),
        ('referral', 'Friend/Family Referral'),
        ('returning', 'Returning Customer'),
        ('social', 'Social Media'),
        ('other', 'Other'),
    ]
    
    # Contact Info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Property Info
    address = models.CharField(max_length=200, blank=True, help_text="Address or neighborhood")
    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICES, blank=True)
    
    # Service Info
    services_needed = models.JSONField(default=list, help_text="Selected services")
    
    # Additional Info
    referral_source = models.CharField(max_length=20, choices=REFERRAL_CHOICES, blank=True)
    message = models.TextField(blank=True)
    
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="Internal notes")

    class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    def get_services_display(self):
        """Return human-readable service names"""
        service_dict = dict(self.SERVICE_CHOICES)
        return [service_dict.get(s, s) for s in self.services_needed]
