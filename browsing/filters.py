import django_filters
from documents.models import Document, ArchObject, DigObject


django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class DocumentListFilter(django_filters.FilterSet):
    document_id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Document


class ArchObjectListFilter(django_filters.FilterSet):

    class Meta:
        model = ArchObject


class DigObjectListFilter(django_filters.FilterSet):

    class Meta:
        model = DigObject
