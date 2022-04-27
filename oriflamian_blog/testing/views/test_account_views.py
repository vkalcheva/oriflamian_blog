from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from oriflamian_blog.account.models import Profile
from oriflamian_blog.ori_app.models import Post

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testuser@test.com',
        'password': '12345qew',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': 'pic.jpg',
        'skin_type': 'skin',
        'age': 'nad 65',
    }

    VALID_POST_DATA = {
        'title': 'The post',
        'photo': 'dsa.jpg',
        'description': 'The test',
        'date_created': date.today(),

    }

    VALID_REVIEW_DATA = {
        'title': 'The review',
        'comment': 'The comment',
        'post_date': date.today(),
    }

    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=self.user)

        # self.review = Review.objects.create(**self.VALID_REVIEW_DATA, user=self.user, post=self.post)

    def test_success_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('login user'))
        self.assertEqual(200, response.status_code)

    def test_edit_profile_view(self):
        user = self.user
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile edit', kwargs={'pk': self.user.pk}))
        self.assertEqual(200, response.status_code)

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 2,
        }))
        self.assertEqual(404, response.status_code)

    def test_when_opening_existing_profile__expect_200(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': self.user.id,
        }))

        self.assertEqual(200, response.status_code)

    def test_get_logged_user_details(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details', kwargs={'pk': self.user.id}))

        posts = list(response.context['posts'])
        profile = self.profile

        self.assertEqual(200, response.status_code)
        self.assertListEqual([], posts)
        self.assertEqual(self.user.id, profile.user_id)

    def test_profile_has_posts(self):
        post = Post.objects.create(**self.VALID_POST_DATA, user=self.user)
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details', kwargs={'pk': self.user.id}))
        user_post = list(response.context['posts'])

        self.assertEqual(200, response.status_code)
        self.assertListEqual([post], user_post)

    # def test_profile_logged_user_change_image(self):
    #     profile = Profile.objects.get(pk=self.user.id)
    #     picture_add = profile.picture
    #     profile.save()
    #     self.client.force_login(self.user)
    #     response = self.client.post(reverse('profile details', kwargs={'pk': self.user.id}))
    #     self.assertEqual(302, response.status_code)

    def test_correct_template(self):
        post = Post.objects.create(**self.VALID_POST_DATA, user=self.user)
        response = self.client.get(reverse('post details', kwargs={'pk': post.pk}))
        self.assertTemplateUsed('ori_app/post_details.html')


