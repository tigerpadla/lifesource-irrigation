from django.shortcuts import render
from .models import Project, ProjectCategory
from newsletter.models import Testimonial


def gallery(request):
    """Display gallery with optional category filter"""
    category_slug = request.GET.get('category')
    
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    
    if category_slug:
        projects = projects.filter(category__slug=category_slug)
    
    # Intersperse testimonials with gallery
    testimonials = Testimonial.objects.filter(is_active=True)
    
    context = {
        'projects': projects,
        'categories': categories,
        'active_category': category_slug,
        'testimonials': testimonials,
    }
    return render(request, 'gallery/gallery.html', context)
