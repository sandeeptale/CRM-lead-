from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from userprofile.models import Userprofile
from lead.models import Lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    # Get or create userprofile for the current user
    userprofile, created = Userprofile.objects.get_or_create(user=request.user)

    # Assuming get_active_team is a method in the Userprofile model
    team = userprofile.get_active_team()

    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
