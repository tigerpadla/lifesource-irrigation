from django.db import models


class ProjectCategory(models.Model):
    """Categories for gallery projects"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Project Categories"
        ordering = ['order']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Gallery project/photo"""
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(ProjectCategory, blank=True, related_name='projects')
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True, help_text="e.g., Upper West Side")
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
