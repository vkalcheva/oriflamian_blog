from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from oriflamian_blog.account.managers import OriflamianUserManager
from oriflamian_blog.common.validators import validate_only_letters


class OriflamianUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = OriflamianUserManager()


class Profile(models.Model):
    UNDER_17 = 'under 17'
    FROM_18_TO_24 = 'от 18 до 24'
    FROM_25_TO_34 = 'от 25 до 34'
    FROM_35_TO_44 = 'от 35 до 44'
    FROM_45_TO_54 = 'от 45 до 54'
    FROM_55_TO_64 = 'от 55 до 64'
    OVER_65 = 'над 65'

    NORMAL_COMBINED = 'normal combined'
    DRY_SENSITIVE = 'dry sensitive'
    OILY = 'oily'

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    picture = models.ImageField(null=True, blank=True,)

    SKIN_TYPE = [(x, x) for x in (NORMAL_COMBINED, DRY_SENSITIVE, OILY)]
    skin_type = models.CharField(
        max_length=max(len(x) for (x, _) in SKIN_TYPE),
        choices=SKIN_TYPE,
    )

    AGES = [(x, x) for x in (UNDER_17, FROM_18_TO_24, FROM_25_TO_34, FROM_35_TO_44, FROM_45_TO_54, FROM_55_TO_64, OVER_65)]
    age = models.CharField(
        max_length=max(len(x) for (x, _) in AGES),
        choices=AGES,
    )

    user = models.OneToOneField(
        OriflamianUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


