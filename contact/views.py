from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """Contact form page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            
            # Send notification email (optional - configure in settings)
            try:
                send_mail(
                    subject=f'New Contact Inquiry from {inquiry.first_name} {inquiry.last_name}',
                    message=f'''
New inquiry received:

Name: {inquiry.first_name} {inquiry.last_name}
Email: {inquiry.email}
Phone: {inquiry.phone}

Services Requested:
{chr(10).join('- ' + s for s in inquiry.get_services_display())}

Message:
{inquiry.message or 'No message provided'}

---
View in admin: /admin/contact/contactinquiry/{inquiry.id}/
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@lifesourceirrigation.com',
                    recipient_list=['info@lifesourceirrigation.com'],
                    fail_silently=True,
                )
            except Exception:
                pass  # Don't fail if email doesn't send
            
            messages.success(request, 'Thank you! We\'ve received your message and will be in touch soon.')
            return redirect('contact:contact_success')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """Contact form success page"""
    return render(request, 'contact/success.html')
