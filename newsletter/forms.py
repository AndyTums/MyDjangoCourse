from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from newsletter.models import Newsletter, Recipient, Message, Try


class StyleFormMixin:
    """ Стилизуем форму """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
                fild.widget.attrs['style'] = 'background-color: #300; color: #5; border-radius: 10px;'
            else:
                fild.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class RecipientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    # def clean_price(self):
    #     """ Проверяем поле цена на отрицательное значение """
    #     price = self.cleaned_data['price']
    #     if price < 0:
    #         raise ValidationError("Цена не может быть отрицательной")
    #     return price

    # def clean(self):
    #     """ Проверяем на поля имя и описание на плохие слова """
    #     list_wrong_worlds = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
    #                          "радар"]
    #     clean_data = super().clean()
    #     name = clean_data.get('name').lower()
    #     description = clean_data.get('description').lower()
    #     if name and description in list_wrong_worlds:
    #         raise ValidationError("Поле не может содержать такие слова")

# class ProductModeratorForm(StyleFormMixin, ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = ['price', 'description', 'name']
