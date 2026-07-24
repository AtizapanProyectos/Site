from django.contrib import admin
from .models import *

for model_name in dir():
    model = globals().get(model_name)
    if model and isinstance(model, type) and issubclass(model, models.Model):
        admin.site.register(model)

