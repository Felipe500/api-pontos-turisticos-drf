from ipware import get_client_ip

from django.http import HttpRequest


def get_ip_and_agent(request: HttpRequest) -> dict:
    try:
        agent = request.META.get('HTTP_USER_AGENT') or ''
        client_ip, _ = get_client_ip(request)
        return {'ip': client_ip, 'agent': agent[:250]}
    except AttributeError:
        return {}