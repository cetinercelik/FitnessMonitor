from django import forms

from settings.models import homemodel, ImagePost, sendMessage


class HomeForm(forms.ModelForm):
    class Meta:
        model = homemodel
        fields = "__all__"

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = "__all__"

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = sendMessage
        fields = "__all__"
