from django.contrib import admin
from .models import Contato


class MemberAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'email')
    list_filter = ('contato',)

admin.site.register(Contato)  # Use the default options