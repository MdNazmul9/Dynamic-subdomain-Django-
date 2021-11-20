from django.shortcuts import render

from .models import Member
from .utilities import get_tanent

def our_team(request):
    tanent = get_tanent(request)
    # print(request)
    members = Member.objects.filter(tanent=tanent)
    return render(request, 'api/our_team.html', {'tanent': tanent, 'members':members }) 