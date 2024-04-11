from django import forms
from .models import Comment, Post
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


MAX_FILE_SIZE = 1048576  # 1MB in bytes


def validate_image_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError("File size too large. Max size is 1MB.")

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'author', 'likes']
        widgets = {
            'featured_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].validators.extend([
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size
        ])


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)