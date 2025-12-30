from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Newsletter, Subscriber


def newsletter_list(request):
    """List all published newsletters"""
    newsletters = Newsletter.objects.filter(is_published=True).order_by('-published_at')
    
    context = {
        'newsletters': newsletters,
    }
    return render(request, 'newsletter/newsletter_list.html', context)


def newsletter_detail(request, slug):
    """Display a single newsletter"""
    newsletter = get_object_or_404(Newsletter, slug=slug, is_published=True)
    
    # Get related newsletters
    related = Newsletter.objects.filter(is_published=True).exclude(id=newsletter.id)[:3]
    
    context = {
        'newsletter': newsletter,
        'related': related,
    }
    return render(request, 'newsletter/newsletter_detail.html', context)


def subscribe(request):
    """Handle newsletter subscription"""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        
        if email:
            subscriber, created = Subscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            
            if created:
                messages.success(request, 'Thanks for subscribing! You\'ll receive our next newsletter.')
            elif not subscriber.is_active:
                subscriber.is_active = True
                subscriber.save()
                messages.success(request, 'Welcome back! You\'ve been re-subscribed.')
            else:
                messages.info(request, 'You\'re already subscribed!')
        else:
            messages.error(request, 'Please enter a valid email address.')
    
    # Redirect back to referring page or home
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)
