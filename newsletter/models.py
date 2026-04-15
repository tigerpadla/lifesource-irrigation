from django.db import models
from django.urls import reverse


class Subscriber(models.Model):
    """Newsletter subscribers"""
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """Newsletter issues / blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300, help_text="Brief summary for listings")
    content = models.TextField()
    image = models.ImageField(upload_to='newsletters/', blank=True, null=True)
    irish_fact = models.TextField(blank=True, help_text="Optional Irish fact/proverb for this issue")
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsletter:newsletter_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True, help_text="e.g., Upper West Side")
    quote = models.TextField()
    project_type = models.CharField(max_length=50, blank=True, help_text="e.g., Rooftop Garden")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        parts = [value for value in [self.client_name, self.location] if value]
        if parts:
            return " - ".join(parts)
        return (self.quote[:37] + "...") if len(self.quote) > 40 else self.quote
