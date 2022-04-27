from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    SKIN_CARE = 'Skin care'
    MAKEUP = 'Makeup'
    FRAGRANCE = 'Fragrance'
    BODY = 'Body'
    HAIR = 'Hair'
    ACCESSORY = 'Accessory'
    WELLNESS = 'Wellness'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (SKIN_CARE, MAKEUP, FRAGRANCE, BODY, HAIR, ACCESSORY, WELLNESS, OTHER)]
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    def __str__(self):
        return f'{self.type}'


class Product(models.Model):
    PRODUCT_NAME_MAX_LEN = 100
    PRICE_MIN_VALUE = 0

    name = models.CharField(
        unique=True,
        max_length=PRODUCT_NAME_MAX_LEN,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    ingredients = models.TextField(
        null=True,
        blank=True,
    )
    how_to_use = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    TITLE_MAX_LEN = 100

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    photo = models.ImageField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    TITLE_MAX_LEN = 15
    COMMENT_MAX_LEN = 1000

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    comment = models.TextField(
        max_length=COMMENT_MAX_LEN,
    )
    post_date = models.DateTimeField(
        auto_now_add=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title + ' | ' + str(self.user)



