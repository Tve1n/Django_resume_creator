from django.db import models


class Resume(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")
    summary = models.TextField(
        verbose_name="О себе",
        help_text="Расскажите о себе"
    )
    education = models.TextField(
        verbose_name="Образование",
        help_text="Учебное заведение"
    )
    experience = models.TextField(
        verbose_name="Опыт работы",
        help_text="Места работы"
    )
    languages = models.TextField(
        verbose_name="Языки",
        blank=True,
        help_text="Какой язык знаете"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
