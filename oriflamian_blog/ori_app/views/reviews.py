from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from oriflamian_blog.ori_app.forms import CreateReviewForm, EditReviewForm
from oriflamian_blog.ori_app.models import Review


class ReviewDetailsView(DetailView):
    model = Review
    template_name = 'ori_app/review_details.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class = CreateReviewForm
    template_name = 'ori_app/review_create.html'

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={'pk': self.object.post_id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = EditReviewForm
    template_name = 'ori_app/review_edit.html'

    def get_success_url(self):
        return reverse_lazy('review details', kwargs={'pk': self.object.id})


class DeleteReviewView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'ori_app/review_delete.html'

    def get_success_url(self):
        return reverse_lazy('post details', kwargs={'pk': self.object.post_id})
