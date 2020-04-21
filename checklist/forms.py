from django import forms
from django.contrib.auth.models import User

from .models import Questionnaire


class QuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        self.fields['q1'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q2'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q3'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q4'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q5'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q6'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q7'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q8'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q9'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q10'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['q11'].widget.attrs.update({'class': 'form-control'})
        self.fields['q12'].widget.attrs.update({'class': 'form-control'})

    q1 = forms.BooleanField(label='Внешний вид', required=False)
    q2 = forms.BooleanField(label='Блок индикации', required=False)
    q3 = forms.BooleanField(label='Осветительные приборы', required=False)
    q4 = forms.BooleanField(label='Звуковой сигнал', required=False)
    q5 = forms.BooleanField(label='Колеса', required=False)
    q6 = forms.BooleanField(label='Стояночный тормоз', required=False)
    q7 = forms.BooleanField(label='Гидравлика', required=False)
    q8 = forms.BooleanField(label='Тормоза', required=False)
    q9 = forms.BooleanField(label='Кресло оператора и ремень безопасности', required=False)
    q10 = forms.BooleanField(label='Рулевое управление', required=False)
    q11 = forms.IntegerField(label='Уровень заряда АКБ')
    q12 = forms.CharField(label='Замечания', required=False)

    class Meta:
        model = Questionnaire
        fields = ('q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12')



class DateForm(forms.Form):
    date = forms.DateInput()