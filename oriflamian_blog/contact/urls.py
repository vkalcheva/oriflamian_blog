from django.urls import path

from oriflamian_blog.contact.views import contact_view

urlpatterns = (
    path('', contact_view, name='contact'),
)