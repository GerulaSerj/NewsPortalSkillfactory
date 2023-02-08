from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок:',
    )
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата создания позднее:',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )
    category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
    )


