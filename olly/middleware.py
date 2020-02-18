from django.shortcuts import render
from ipware import get_client_ip

from profiles.models import UserProfile, BannedUser


def tenant_middleware(get_response):
    def middleware(request):

        host = request.get_host()
        subdomain = host.split('.')[0]
        domain = host.split('.')[-2]

        if domain == 'nfmstudios' or subdomain == 'nfm':
            request.tenant = 'stock'

        else:
            request.tenant = 'stock'

        # all done, the view will receive a request with a tenant attribute
        return get_response(request)

    return middleware


def ban_middleware(get_response):
    def middleware(request):
        ip = get_client_ip(request)
        ip = ip[0]

        if not (request.path_info == '/profile/banned/' and not request.path_info == '/admin'):
            if ip is not None:
                if not request.user.is_anonymous:
                    user = UserProfile.objects.get(user__username=request.user.username)
                    user.ip = ip  # change field
                    user.save()  # this will update only
                    if not BannedUser.objects.filter(ip=ip).exists():
                        if BannedUser.objects.filter(user=request.user):
                            return render(request, 'profiles/' + request.tenant + '/banned.html')
                if BannedUser.objects.filter(ip=ip).exists():
                    return render(request, 'profiles/' + request.tenant + '/banned.html')

        return get_response(request)

    return middleware
