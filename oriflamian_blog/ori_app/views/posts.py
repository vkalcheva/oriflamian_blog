from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from oriflamian_blog.ori_app.forms import CreatePostForm, EditPostForm
from oriflamian_blog.ori_app.models import Post


class PostDetailsView(DetailView):
    model = Post
    template_name = 'ori_app/post_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'ori_app/post_create.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={'pk': self.object.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('you not authorised')
        return super().dispatch(request, *args, **kwargs)


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'ori_app/post_edit.html'
    form_class = EditPostForm

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={'pk': self.object.id})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('you not authorised')
        return super().dispatch(request, *args, **kwargs)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'ori_app/post_delete.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('you not authorised')
        return super().dispatch(request, *args, **kwargs)





