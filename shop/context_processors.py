from django.conf import settings

def user_variables(request):
	return {
			'SITE_NAME': settings.SITE_NAME,
			}