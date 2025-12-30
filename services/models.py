from django.db import models
from django.urls import reverse


class ServiceCategory(models.Model):
    """Main service categories: Irrigation, Gardening, Lighting, Terrace Refurbishment"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=200, help_text="Brief description for cards")
    full_description = models.TextField(help_text="Detailed description for service page")
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class, e.g., 'bi-droplet'")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='services/heroes/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})


class SubService(models.Model):
    """Sub-services under each category, e.g., Design & Installation under Irrigation"""
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='sub_services')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class")
    image = models.ImageField(upload_to='services/sub/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.category.title} - {self.title}"
