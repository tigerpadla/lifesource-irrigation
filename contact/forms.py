from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit, HTML, Div
from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    """Smart contact form with service selection"""
    
    # Service checkboxes - will be handled separately in template
    services_needed = forms.MultipleChoiceField(
        choices=ContactInquiry.SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Services Needed (select all that apply)"
    )
    
    class Meta:
        model = ContactInquiry
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'services_needed', 'referral_source', 'message'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'referral_source': 'How did you hear about us?',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Contact Information',
                Row(
                    Column('first_name', css_class='col-md-6'),
                    Column('last_name', css_class='col-md-6'),
                ),
                Row(
                    Column('email', css_class='col-md-6'),
                    Column('phone', css_class='col-md-6'),
                ),
            ),
            Fieldset(
                'How Can We Help?',
                'services_needed',
            ),
            Fieldset(
                'Additional Information',
                'referral_source',
                'message',
            ),
            Div(
                Submit('submit', 'Send Message', css_class='btn btn-success btn-lg px-5'),
                css_class='text-center mt-4'
            )
        )
        
        # Add placeholders and styling
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['phone'].widget.attrs['placeholder'] = '(212) 555-0123'
        self.fields['message'].widget.attrs['placeholder'] = 'Tell us about your project...'
