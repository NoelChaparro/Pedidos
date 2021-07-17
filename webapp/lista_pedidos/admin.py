from django.apps import apps
from django.contrib import admin

app_config = apps.get_app_config('lista_pedidos')
models = app_config.get_models()

for model in models:
	try:
		admin.site.register(model)
	except admin.sites.AlreadyRegistered:
		pass