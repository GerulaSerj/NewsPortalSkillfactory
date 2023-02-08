from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'categoryType',
           'postCategory',
           'title',
           'text',
       ]

       def clean(self):
           cleaned_data = super().clean()
           text = cleaned_data.get("text")
           if text is not None and len(text) < 20:
               raise ValidationError({
                   "text": "Описание не может быть менее 20 символов."
               })

           title = cleaned_data.get("title")
           if title == text:
               raise ValidationError(
                   "Описание не должно быть идентично названию."
               )

           return cleaned_data


class ArticlesForm(forms.Form):
    class Meta:
        model = Post
        fields = [
            'postCategory',
            'title',
            'text',
        ]

        def clean(self):
            cleaned_data = super().clean()
            text = cleaned_data.get("text")
            if text is not None and len(text) < 20:
                raise ValidationError({
                    "text": "Описание не может быть менее 20 символов."
                })

            title = cleaned_data.get("title")
            if title == text:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data