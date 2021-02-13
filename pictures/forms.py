from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from .handlers import check_proportions
from .models import Picture


class PictureForm(forms.ModelForm):

    def clean(self):
        image = self.cleaned_data['image']
        link = self.cleaned_data['link']
        if link and image:
            raise ValidationError(_('Заполнены все 2 поля, а нужно 1.'))
        if not link and not image:
            raise ValidationError(_('Не заполнено ни одного поля.'))
        return self.cleaned_data

    class Meta:
        model = Picture
        fields = ['link', 'image', ]


class ResizeForm(forms.ModelForm):

    def clean(self):
        old_picture = get_object_or_404(Picture, id=self.initial['picture_id'])
        old_width = old_picture.width
        old_height = old_picture.height
        width = self.cleaned_data['width']
        height = self.cleaned_data['height']
        if not width and not height:
            raise ValidationError(_('Введите хотя бы 1 размер.'))
        if not check_proportions(old_width, old_height, width, height):
            raise ValidationError(_(
                'Введенные ширина и высота не совпадают с оригинальными '
                'пропорциями. Фотография не будет сохранена в базу.'
                ''))
        return self.cleaned_data

    class Meta:
        model = Picture
        fields = ['width', 'height', ]
