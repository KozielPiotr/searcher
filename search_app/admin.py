"""Options for admin site"""

from django.contrib import admin

from .models import Search


admin.site.register(Search)
