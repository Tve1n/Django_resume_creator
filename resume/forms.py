from django import forms
from .models import Resume
import re

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'full_name', 'email', 'phone', 'address',
            'summary', 'education', 'experience', 'languages'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'some_email@mail.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7(000)000-00-00'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ваш адрес'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Расскажите о себе'
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Название заведения, специальность, годы обучения'
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Места работы, должности, обязанности, достижения'
            }),
            'languages': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Русский, Английский'
            }),
        }
        labels = {
            'full_name': 'ФИО',
            'email': 'Email',
            'phone': 'Телефон',
            'address': 'Адрес',
            'summary': 'О себе',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'languages': 'Языки',
        }
        error_messages = {
            'full_name': {
                'required': 'Поле "Полное имя" обязательно для заполнения',
            },
            'email': {
                'required': 'Поле "Email" обязательно для заполнения',
                'invalid': 'Введите корректный email адрес',
            },
            'phone': {
                'required': 'Поле "Телефон" обязательно для заполнения',
            }
        }
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        
        # Удаляем все кроме цифр
        clean_phone = re.sub(r'\D', '', phone)
        
        if len(clean_phone) != 11:
            raise forms.ValidationError('Номер телефона должен содержать ровно 11 цифр')
        
        if not clean_phone.startswith(('7', '8')):
            raise forms.ValidationError('Номер телефона должен начинаться с 7 или 8')
        
        return clean_phone
    
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()
        
        if len(full_name.split()) < 2:
            raise forms.ValidationError('Введите фамилию и имя (минимум 2 слова)')

        for word in full_name.split():
            if not word[0].isupper():
                raise forms.ValidationError('Каждое слово в ФИО должно начинаться с заглавной буквы')
        
        return full_name