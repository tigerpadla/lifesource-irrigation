from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, SubService


# Default service data for initial display before database is populated
DEFAULT_SERVICES = {
    'irrigation': {
        'title': 'Irrigation',
        'short_description': 'Installations, maintenance, and repairs for hands-off plant hydration.',
        'full_description': '''Our irrigation services ensure your plants receive the perfect amount of water, 
        automatically. From drip irrigation systems for rooftop gardens to full sprinkler installations 
        for lawns, we design, install, and maintain systems that keep your green spaces thriving with 
        minimal effort on your part.''',
        'icon': 'bi-droplet-fill',
        'sub_services': [
            {
                'title': 'Design & Installation',
                'description': 'Custom irrigation system design tailored to your space. We assess your plants, layout, and water needs to create an efficient system that delivers precise hydration to every corner of your garden.',
                'icon': 'bi-pencil-square'
            },
            {
                'title': 'Seasonal Maintenance',
                'description': 'Spring startup, mid-season adjustments, and winterization services. We ensure your system is ready for each season and protected from freeze damage.',
                'icon': 'bi-calendar-check'
            },
            {
                'title': 'Repairs & Upgrades',
                'description': 'Fast, reliable repairs for leaks, broken heads, and controller issues. We also upgrade older systems with smart controllers and water-efficient components.',
                'icon': 'bi-wrench'
            },
        ]
    },
    'gardening': {
        'title': 'Gardening',
        'short_description': 'Transformations and tender care for sacred green spaces, from bulbs to blooms.',
        'full_description': '''Our gardening services bring life and beauty to your outdoor spaces. Whether 
        you're dreaming of a lush rooftop retreat or need ongoing care for an established garden, our 
        experienced team transforms and maintains gardens that inspire.''',
        'icon': 'bi-flower1',
        'sub_services': [
            {
                'title': 'Design & Installation',
                'description': 'Complete garden design and planting services. We select plants suited to NYC\'s unique microclimates and your space\'s specific conditions—sun, wind, and weight considerations for rooftops.',
                'icon': 'bi-pencil-square'
            },
            {
                'title': 'Seasonal Maintenance',
                'description': 'Regular care including pruning, fertilizing, mulching, and seasonal plantings. We keep your garden looking its best year-round with scheduled maintenance visits.',
                'icon': 'bi-calendar-check'
            },
            {
                'title': 'Holiday Décor',
                'description': 'Festive seasonal decorations for your outdoor spaces. From spring planters to winter holiday displays, we bring seasonal cheer to your terrace or garden.',
                'icon': 'bi-gift'
            },
        ]
    },
    'lighting': {
        'title': 'Lighting',
        'short_description': 'Customized lighting design to extend garden enjoyment long after the sun has set.',
        'full_description': '''Extend the enjoyment of your outdoor spaces into the evening hours with our 
        professional landscape lighting services. We design and install low-voltage lighting systems that 
        highlight your garden's best features while providing safety and ambiance.''',
        'icon': 'bi-lightbulb-fill',
        'sub_services': [
            {
                'title': 'Design & Installation',
                'description': 'Custom lighting design that enhances your garden\'s beauty after dark. We use quality LED fixtures and smart controls for stunning effects and energy efficiency.',
                'icon': 'bi-pencil-square'
            },
            {
                'title': 'Path & Safety Lighting',
                'description': 'Illuminate walkways, stairs, and transitions for safe navigation. Subtle fixtures that blend with your landscape while providing essential visibility.',
                'icon': 'bi-signpost'
            },
            {
                'title': 'Accent & Feature Lighting',
                'description': 'Highlight trees, sculptures, water features, and architectural elements. Create dramatic focal points and extend your living space into the night.',
                'icon': 'bi-stars'
            },
        ]
    },
    'terrace-refurbishment': {
        'title': 'Terrace Refurbishment',
        'short_description': 'Complete terrace renewal including power washing, repairs, and surface restoration.',
        'full_description': '''Bring new life to tired terraces and outdoor surfaces. Our refurbishment services 
        address everything from deep cleaning to structural repairs, ensuring your outdoor space is safe, 
        beautiful, and ready for enjoyment.''',
        'icon': 'bi-hammer',
        'sub_services': [
            {
                'title': 'Power Washing',
                'description': 'Professional pressure washing for pavers, decking, walls, and furniture. Remove years of grime, algae, and stains to restore surfaces to like-new condition.',
                'icon': 'bi-water'
            },
            {
                'title': 'Surface Repairs',
                'description': 'Fix cracked pavers, damaged decking, and deteriorating surfaces. We repair or replace problem areas to ensure safety and aesthetics.',
                'icon': 'bi-tools'
            },
            {
                'title': 'Demolition & Prep',
                'description': 'Removal of old planters, damaged structures, and overgrown plantings. We prepare your space for renovation or complete transformation.',
                'icon': 'bi-trash3'
            },
        ]
    },
}


def service_list(request):
    """Display all service categories"""
    services = ServiceCategory.objects.filter(is_active=True).order_by('order')
    
    # If no services in database, use defaults
    if not services.exists():
        services = [
            {'slug': slug, **data} 
            for slug, data in DEFAULT_SERVICES.items()
        ]
    
    context = {
        'services': services,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, slug):
    """Display a single service category with its sub-services"""
    try:
        service = get_object_or_404(ServiceCategory, slug=slug, is_active=True)
        sub_services = service.sub_services.filter(is_active=True).order_by('order')
        from_db = True
    except:
        # Fallback to default data
        if slug in DEFAULT_SERVICES:
            service = {'slug': slug, **DEFAULT_SERVICES[slug]}
            sub_services = DEFAULT_SERVICES[slug]['sub_services']
            from_db = False
        else:
            from django.http import Http404
            raise Http404("Service not found")
    
    # Get all services for sidebar navigation
    all_services = ServiceCategory.objects.filter(is_active=True).order_by('order')
    if not all_services.exists():
        all_services = [{'slug': s, 'title': DEFAULT_SERVICES[s]['title']} for s in DEFAULT_SERVICES]
    
    context = {
        'service': service,
        'sub_services': sub_services,
        'all_services': all_services,
        'from_db': from_db if 'from_db' in dir() else False,
    }
    return render(request, 'services/service_detail.html', context)
