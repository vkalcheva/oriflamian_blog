from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, RedirectView

from oriflamian_blog.account.forms import CreateProfileForm, EditProfileForm, ChangePasswordForm
from oriflamian_blog.account.models import Profile
from oriflamian_blog.ori_app.models import Post


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'account/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user_id=self.request.user.id)

        return context


class UserRegistrationView(CreateView):
    form_class = CreateProfileForm
    template_name = 'account/register_page.html'
    success_url = reverse_lazy('login user')


class UserLoginView(LoginView):
    template_name = 'account/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login user')


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'account/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class ChangeUserPasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_success')
    template_name = 'account/change_password.html'






