from django.shortcuts import render
from services.models import ServiceCategory
from gallery.models import Project
from newsletter.models import Testimonial


def home(request):
    """Home page view"""
    services = ServiceCategory.objects.filter(is_active=True).order_by('order')[:3]
    projects = Project.objects.filter(featured=True).order_by('-created_at')[:8]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-created_at')[:10]
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)
