from django.contrib import admin
from .models import branches
from .models import departments

# Register your models here.
admin.site.register(branches)
admin.site.register(departments)