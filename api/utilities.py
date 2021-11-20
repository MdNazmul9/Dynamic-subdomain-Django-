from .models import Tanent

def get_hontname(request):
    return request.get_host().split(':')[0].lower()

def get_tanent(request):
    hostname = get_hontname(request)
    subdomain = hostname.split('.')[0]
    # print(subdomain)
    return Tanent.objects.filter(subdomain=subdomain).first()

    

    
