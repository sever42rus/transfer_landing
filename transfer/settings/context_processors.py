from settings.models import Setting

def get_setting(request):
	setting = Setting.objects.all().first()
	return {'setting': setting}