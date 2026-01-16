# Generated data migration to populate default project categories

from django.db import migrations


def create_default_categories(apps, schema_editor):
    """Create the 4 default project categories for the gallery."""
    ProjectCategory = apps.get_model('gallery', 'ProjectCategory')
    
    categories = [
        {'name': 'Irrigation', 'slug': 'irrigation', 'order': 1},
        {'name': 'Gardening', 'slug': 'gardening', 'order': 2},
        {'name': 'Lighting', 'slug': 'lighting', 'order': 3},
        {'name': 'Terrace Refurbishment', 'slug': 'terrace-refurbishment', 'order': 4},
    ]
    
    for cat in categories:
        ProjectCategory.objects.get_or_create(
            slug=cat['slug'],
            defaults={'name': cat['name'], 'order': cat['order']}
        )


def remove_default_categories(apps, schema_editor):
    """Remove the default categories (reverse migration)."""
    ProjectCategory = apps.get_model('gallery', 'ProjectCategory')
    ProjectCategory.objects.filter(
        slug__in=['irrigation', 'gardening', 'lighting', 'terrace-refurbishment']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, remove_default_categories),
    ]
