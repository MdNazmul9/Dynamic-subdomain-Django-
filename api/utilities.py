from .models import Institute

def get_hontname(request):
    return request.get_host().split(':')[0].lower()

def get_institute(request):
    hostname = get_hontname(request)
    subdomain = hostname.split('.')[0]
    # print(subdomain)
    return Institute.objects.filter(subdomain=subdomain).first()

    

    
