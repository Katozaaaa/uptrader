from django.db import models

class Menu(models.Model):
    parent = models.ForeignKey(
        'Menu', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Родитель', 
        help_text='Определяет, к какому разделу принадлежит данный пункт меню. Если значение не указано, то пункт считается заглавным.'
    )
    name = models.CharField(max_length=100, primary_key=True, unique=True, verbose_name='Название', 
        help_text='Определяет имя пункта меню.'
    )
    slug = models.SlugField(
        max_length=100, unique=True, db_index=True, verbose_name='URL',
        help_text='Определяет slug пункта меню.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = verbose_name