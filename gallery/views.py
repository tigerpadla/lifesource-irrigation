import random
from collections import OrderedDict
from django.shortcuts import render
from .models import Project, ProjectCategory
from newsletter.models import Testimonial

# Season display order and metadata
SEASON_ORDER = ['spring', 'summer', 'fall', 'winter']
SEASON_META = {
    'spring': {'label': 'Spring', 'icon': 'bi-flower2', 'description': 'Fresh beginnings and new growth'},
    'summer': {'label': 'Summer', 'icon': 'bi-sun', 'description': 'Lush gardens in full bloom'},
    'fall': {'label': 'Fall', 'icon': 'bi-wind', 'description': 'Golden tones and seasonal transitions'},
    'winter': {'label': 'Winter', 'icon': 'bi-snow', 'description': 'Winter care and preparation'},
}


def _intersperse_testimonials(projects, testimonials, start_index):
    """
    Intersperse testimonials into project list using row-based logic.
    Testimonials appear on every second row (rows 2, 4, 6...).
    Each testimonial row has 4 slots (3 projects + 1 testimonial).
    Non-testimonial rows have 4 projects.
    Testimonial is never in position 0 (first), randomly placed in positions 1-3.
    Testimonial position never repeats from the previous testimonial row to avoid stacking.
    Returns (items_list, next_testimonial_index).
    """
    items = []
    t_index = start_index
    last_testimonial_pos = -1
    row_number = 0
    
    project_index = 0
    while project_index < len(projects):
        row_number += 1
        is_testimonial_row = (row_number % 2 == 0)
        
        if is_testimonial_row and t_index < len(testimonials):
            # Testimonial row: 3 projects + 1 testimonial
            row_projects = projects[project_index:project_index + 3]
            project_index += len(row_projects)
            
            if len(row_projects) >= 2:
                row_items = [{'type': 'project', 'data': p} for p in row_projects]
                testimonial_item = {'type': 'testimonial', 'data': testimonials[t_index]}
                
                # Random position (never first/0), avoid same column as last testimonial row
                possible_positions = [i for i in range(1, len(row_items) + 1) if i != last_testimonial_pos]
                if not possible_positions:
                    possible_positions = list(range(1, len(row_items) + 1))
                insert_pos = random.choice(possible_positions)
                last_testimonial_pos = insert_pos
                
                row_items.insert(insert_pos, testimonial_item)
                items.extend(row_items)
                t_index += 1
            else:
                items.extend([{'type': 'project', 'data': p} for p in row_projects])
        else:
            # Non-testimonial row: 4 projects
            row_projects = projects[project_index:project_index + 4]
            project_index += len(row_projects)
            items.extend([{'type': 'project', 'data': p} for p in row_projects])
    
    return items, t_index


def gallery(request):
    """Display gallery grouped by season with scattered testimonials"""
    category_slug = request.GET.get('category')
    
    categories = ProjectCategory.objects.all()
    projects = Project.objects.prefetch_related('additional_images').all()
    
    if category_slug:
        projects = projects.filter(categories__slug=category_slug).distinct()
    
    # Get active testimonials and shuffle them
    testimonials = list(Testimonial.objects.filter(is_active=True))
    random.shuffle(testimonials)
    testimonial_index = 0
    
    # Group projects by season in the correct order
    season_groups = OrderedDict()
    for season_key in SEASON_ORDER:
        season_projects = [p for p in projects if p.season == season_key]
        if season_projects:
            items, testimonial_index = _intersperse_testimonials(
                season_projects, testimonials, testimonial_index
            )
            season_groups[season_key] = {
                'meta': SEASON_META[season_key],
                'items': items,
            }
    
    # Collect any uncategorized projects (no season assigned)
    uncategorized = [p for p in projects if not p.season]
    if uncategorized:
        items, testimonial_index = _intersperse_testimonials(
            uncategorized, testimonials, testimonial_index
        )
        season_groups['uncategorized'] = {
            'meta': {'label': 'Other Projects', 'icon': 'bi-images', 'description': ''},
            'items': items,
        }
    
    # Flatten all projects for the modal JSON data
    all_projects = list(projects)
    
    context = {
        'season_groups': season_groups,
        'projects': all_projects,
        'categories': categories,
        'active_category': category_slug,
    }
    return render(request, 'gallery/gallery.html', context)
