from user_agents import parse


def get_client_browser_ip(request):
    """ get ip and browser info from request """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    browser = request.META['HTTP_USER_AGENT']
    user_agent = parse(browser)
    return ip, user_agent.browser
