from django.forms import ModelForm
from captcha.fields import CaptchaField
from guest_book.models import Message, CustomUser
from file_resubmit.admin import AdminResubmitImageWidget


class UserForm(ModelForm):
    """
    Create form from Custom user model with username and email field
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class MessageForm(ModelForm):
    """Create message form, include CAPTCHA from andmm link,
    message and image fields"""
    captcha = CaptchaField()

    class Meta:
        model = Message
        fields = ['link', 'message', 'image']
        widgets = {
            'image': AdminResubmitImageWidget,
        }

