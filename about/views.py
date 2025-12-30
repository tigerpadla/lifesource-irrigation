from django.shortcuts import render
from .models import TeamMember, IrishFact


def about(request):
    """About page with team and Irish heritage"""
    team_members = TeamMember.objects.filter(is_active=True)
    irish_facts = IrishFact.objects.filter(is_active=True)[:3]
    
    context = {
        'team_members': team_members,
        'irish_facts': irish_facts,
    }
    return render(request, 'about/about.html', context)
