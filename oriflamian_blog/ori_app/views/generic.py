from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from oriflamian_blog.ori_app.models import Post


class HomeView(TemplateView):
    template_name = 'ori_app/home_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    model = Post
    template_name = 'ori_app/dashboard.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

