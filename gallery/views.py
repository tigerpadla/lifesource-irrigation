import random
from collections import OrderedDict
from django.shortcuts import render
from .models import Project, ProjectCategory
from newsletter.models import Testimonial

# Season display order and metadata
SEASON_ORDER = ['spring', 'summer', 'fall', 'winter', 'holiday']
SEASON_META = {
    'spring': {'label': 'Spring', 'icon': 'bi-flower2', 'description': 'Fresh beginnings and new growth'},
    'summer': {'label': 'Summer', 'icon': 'bi-sun', 'description': 'Lush gardens in full bloom'},
    'fall': {'label': 'Fall', 'icon': 'bi-wind', 'description': 'Golden tones and seasonal transitions'},
    'winter': {'label': 'Winter', 'icon': 'bi-snow', 'description': 'Winter care and preparation'},
    'holiday': {'label': 'Holiday Decor', 'icon': 'bi-gift-fill', 'description': 'Festive seasonal decorations'},
}


def _intersperse_testimonials(projects, testimonials, start_index):
    """
    Intersperse testimonials into project list using row-based logic.
    Each row has 4 slots (3 projects + 1 testimonial).
    Testimonial is never in position 0 (first), randomly placed in positions 1-3.
    Testimonial position never repeats from the previous row to avoid stacking.
    Returns (items_list, next_testimonial_index).
    """
    items = []
    t_index = start_index
    row_size = 4
    last_testimonial_pos = -1
    
    project_index = 0
    while project_index < len(projects):
        # Get up to 3 projects for this row (leaving room for 1 testimonial)
        row_projects = projects[project_index:project_index + (row_size - 1)]
        project_index += len(row_projects)
        
        if t_index < len(testimonials) and len(row_projects) >= 2:
            row_items = [{'type': 'project', 'data': p} for p in row_projects]
            testimonial_item = {'type': 'testimonial', 'data': testimonials[t_index]}
            
            # Random position (never first/0), avoid same column as last row
            possible_positions = [i for i in range(1, len(row_items) + 1) if i != last_testimonial_pos]
            if not possible_positions:
                possible_positions = list(range(1, len(row_items) + 1))
            insert_pos = random.choice(possible_positions)
            last_testimonial_pos = insert_pos
            
            row_items.insert(insert_pos, testimonial_item)
            items.extend(row_items)
            t_index += 1
        else:
            # No more testimonials or not enough projects for a full row
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
