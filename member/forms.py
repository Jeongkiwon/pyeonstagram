from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '휴대폰 번호 또는 이메일 주소',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '비밀번호',
        })


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['user_id','name','username','password1', 'password2']

        self.fields['user_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder':'사용자 이름',
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '성명',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '휴대폰 번호 또는 이메일 주소',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '비밀번호',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '비밀번호 재입력',
        })

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'user_id',
            'password1',
            'password2',

        )

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }