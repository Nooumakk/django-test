from django import forms
from .models import Feadback


class FormFeadback(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs = {
                "class": "form-control", "placeholder": "Ваше имя", 
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {
                "class": "form-control", "placeholder": "Электронная почта", 
            }
        )
    )
    message = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class": "form-control", "placeholder": "Сообщение", 
            }
        )
    )

    def clean(self):
        has_error = False
        if self.cleaned_data["name"] in ("admin", "superadmin"):
            self.add_error("name", "Впишите настоящее имя")
            has_error = True
        if len(self.cleaned_data["message"]) > 1000:
            self.add_error("message", "Слишком длинное сообщение, постарайтесь уложится в 1000 символов")
            has_error = True
        if not has_error:
            self.save()
        else:
            raise forms.ValidationError("Неверные данные")
        return self.cleaned_data
    
    def save(self):
        Feadback.objects.create(**self.cleaned_data)