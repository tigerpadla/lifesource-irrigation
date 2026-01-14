from django.shortcuts import render
from services.models import ServiceCategory
from gallery.models import Project
from newsletter.models import Testimonial
import random


def home(request):
    """Home page view"""
    services = ServiceCategory.objects.filter(is_active=True).order_by('order')[:3]
    projects = list(Project.objects.filter(featured=True).order_by('-created_at')[:6])
    testimonials = list(Testimonial.objects.filter(is_active=True).order_by('-created_at')[:10])
    
    # Build gallery items with interspersed testimonials (one per row of 4)
    gallery_items = []
    random.shuffle(testimonials)
    testimonial_index = 0
    last_testimonial_pos = None
    
    # Process in rows of 4 (3 projects + 1 testimonial per row)
    project_index = 0
    row_count = 0
    
    while project_index < len(projects) and testimonial_index < len(testimonials):
        # Get up to 3 projects for this row
        row_projects = projects[project_index:project_index + 3]
        row_items = [{'type': 'project', 'item': p} for p in row_projects]
        project_index += 3
        
        # Insert testimonial at random position (never first, avoiding same column as last row)
        possible_positions = [i for i in range(1, len(row_items) + 1) if i != last_testimonial_pos]
        insert_pos = random.choice(possible_positions) if possible_positions else random.randint(1, len(row_items))
        
        row_items.insert(insert_pos, {'type': 'testimonial', 'item': testimonials[testimonial_index]})
        testimonial_index += 1
        last_testimonial_pos = insert_pos
        
        gallery_items.extend(row_items)
        row_count += 1
    
    context = {
        'services': services,
        'gallery_items': gallery_items,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)
