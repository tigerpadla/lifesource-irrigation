from django.db import models


class TeamMember(models.Model):
    """Team member profiles"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class IrishFact(models.Model):
    """Irish-American corner facts/songs/history"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('fact', 'Fun Fact'),
        ('song', 'Traditional Song'),
        ('history', 'History'),
        ('proverb', 'Irish Proverb'),
    ], default='fact')
    image = models.ImageField(upload_to='irish/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
