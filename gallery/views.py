import random
from django.shortcuts import render
from .models import Project, ProjectCategory
from newsletter.models import Testimonial


def gallery(request):
    """Display gallery with optional category filter and interspersed testimonials"""
    category_slug = request.GET.get('category')
    
    categories = ProjectCategory.objects.all()
    projects = list(Project.objects.all())
    
    if category_slug:
        projects = list(Project.objects.filter(category__slug=category_slug))
    
    # Get active testimonials and shuffle them
    testimonials = list(Testimonial.objects.filter(is_active=True))
    random.shuffle(testimonials)
    
    # Place one testimonial per row (4 columns)
    # Each row will have 3 images + 1 testimonial at a random position
    gallery_items = []
    testimonial_index = 0
    row_size = 4
    last_testimonial_pos = -1  # Track last position to avoid stacking
    
    # Process projects in chunks to create rows
    project_index = 0
    while project_index < len(projects):
        # Get up to 3 projects for this row (leaving room for 1 testimonial)
        row_projects = projects[project_index:project_index + (row_size - 1)]
        project_index += len(row_projects)
        
        # If we have a testimonial to add, insert it at a random position in the row
        if testimonial_index < len(testimonials):
            row_items = [{'type': 'project', 'data': p} for p in row_projects]
            testimonial_item = {'type': 'testimonial', 'data': testimonials[testimonial_index]}
            
            # Random position (never first), but avoid same position as last row
            possible_positions = [i for i in range(1, len(row_items) + 1) if i != last_testimonial_pos]
            insert_pos = random.choice(possible_positions) if possible_positions else random.randint(1, len(row_items))
            last_testimonial_pos = insert_pos
            
            row_items.insert(insert_pos, testimonial_item)
            
            gallery_items.extend(row_items)
            testimonial_index += 1
        else:
            # No more testimonials, just add the projects
            gallery_items.extend([{'type': 'project', 'data': p} for p in row_projects])
    
    context = {
        'gallery_items': gallery_items,
        'projects': projects,
        'categories': categories,
        'active_category': category_slug,
    }
    return render(request, 'gallery/gallery.html', context)
