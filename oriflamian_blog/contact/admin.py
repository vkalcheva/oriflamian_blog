from django.contrib import admin

from oriflamian_blog.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
