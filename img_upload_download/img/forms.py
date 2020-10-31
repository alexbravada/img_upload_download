from django.forms import ModelForm
from .models import Img


class ImgUpload(ModelForm):
    class Meta:
        model = Img
        exclude = ['is_active']
