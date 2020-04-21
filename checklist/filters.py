import django_filters
from django_filters.widgets import RangeWidget

from .models import Questionnaire


class QuestionnaireFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name='date', lookup_expr='iexact', widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD','class':'form-control'}))

    class Meta:
        model = Questionnaire
        fields = ['date']
