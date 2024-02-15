from .models import Team

def team(request):
    if request.user.is_authenticated:
        user_profile = getattr(request.user, 'userprofile', None)
        active_team = user_profile.get_active_team() if user_profile else None
    else:
        active_team = None

    return {'active_team': active_team}
