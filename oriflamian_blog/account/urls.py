from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from oriflamian_blog.account.views import UserRegistrationView, UserLoginView, UserLogoutView, ChangeUserPasswordView, \
    ProfileDetailsView, EditProfileView

urlpatterns = (

    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('profile/edit/password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_success'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),

)


