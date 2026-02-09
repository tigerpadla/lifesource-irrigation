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
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ]
    
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(ProjectCategory, blank=True, related_name='projects')
    season = models.CharField(
        max_length=20, 
        choices=SEASON_CHOICES, 
        blank=True, 
        help_text="Assign a season to group photos in the gallery"
    )
    image = models.ImageField(upload_to='gallery/', help_text="Main/cover image for this project")
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True, help_text="e.g., Upper West Side")
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.PositiveIntegerField(default=0, help_text="Order within the season section (lower = first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
    
    def get_all_images(self):
        """Return all images for this project (main + additional)"""
        images = [{'url': self.image.url, 'is_main': True}]
        for img in self.additional_images.all():
            images.append({'url': img.image.url, 'is_main': False, 'caption': img.caption})
        return images
    
    @property
    def image_count(self):
        """Total number of images (main + additional)"""
        return 1 + self.additional_images.count()


class ProjectImage(models.Model):
    """Additional images for a gallery project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption for this image")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower = first)")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Additional Image"
        verbose_name_plural = "Additional Images"

    def __str__(self):
        return f"{self.project.title} - Image {self.order + 1}"
