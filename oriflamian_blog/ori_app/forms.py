from django import forms

from oriflamian_blog.common.helpers import BootstrapFormMixin
from oriflamian_blog.ori_app.models import Post, Review


class CreatePostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.user
        if commit:
            post.save()
        return post

    class Meta:
        model = Post
        fields = ('title', 'photo', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter post name',
                }
            ),
        }


class EditPostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Post
        exclude = ('user',)


class CreateReviewForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        review = super().save(commit=False)
        review.user = self.user
        if commit:
            review.save()
        return review

    class Meta:
        model = Review
        fields = ('title', 'comment', 'post')


class EditReviewForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        exclude = ('user',)





