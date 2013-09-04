from django.middleware.csrf import CsrfViewMiddleware


class CustomCsrfViewMiddleware(CsrfViewMiddleware):
    """
    Middleware that requires a present and correct csrfmiddlewaretoken
    for POST requests that have a CSRF cookie, and sets an outgoing
    CSRF cookie.

    This middleware should be used in conjunction with the csrf_token template
    tag.
    """

    def process_template_response(self, request, response):
        """

        :param request:
        :param response:
        """
        if request.META.get('CSRF_COOKIE_USED', False):
            response.Context["csrf_token"] = request.META['CSRF_COOKIE']
