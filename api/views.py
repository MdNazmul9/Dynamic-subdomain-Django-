from django.shortcuts import render

from .models import Member
from .utilities import get_institute

def institute_view(request):
    institute = get_institute(request)
    # print(request)
    members = Member.objects.filter(institute=institute)
    return render(request, 'api/our_team.html', {'institute': institute, 'members':members }) 