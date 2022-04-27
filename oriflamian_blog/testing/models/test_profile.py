from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from oriflamian_blog.account.models import Profile

UserModel = get_user_model()


class ProfileTest(TestCase):
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

    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=self.user)

    def test_create_profile__when_first_name_contain_only_letters_expect_success(self):
        profile = self.profile
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_create_profile__when_first_name_contain_digit_expect_fail(self):
        first_name = 'Test1'

        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            picture=self.VALID_PROFILE_DATA['picture'],
            skin_type=self.VALID_PROFILE_DATA['skin_type'],
            age=self.VALID_PROFILE_DATA['age'],
            user=self.user,

        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)


    def test_create_profile__when_first_name_contain_dollar_sign_expect_fail(self):
        first_name = 'Tes$t'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            picture=self.VALID_PROFILE_DATA['picture'],
            skin_type=self.VALID_PROFILE_DATA['skin_type'],
            age=self.VALID_PROFILE_DATA['age'],
            user=self.user,

        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid_expect_correct_full_name(self):
        user = self.user
        profile = self.profile
        self.assertEqual('Test User', profile.full_name)
