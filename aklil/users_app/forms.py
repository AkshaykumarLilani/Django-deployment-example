from django import forms
from users_app.models import Users

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
