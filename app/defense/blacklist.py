from defense.models import Defense


def Blacklist(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    found_ip = Defense.objects.filter(ip=ip).exists()
   
    if found_ip:
        return True
    
    return False
    