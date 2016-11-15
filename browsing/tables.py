import django_tables2 as tables
from django_tables2.utils import A
from documents.models import Document


class DocumentTable(tables.Table):
    document_id = tables.LinkColumn(
        'documents:document_detail', args=[A('pk')], verbose_name='URI')
    doucment_type = tables.Column(verbose_name='Document Type')

    class Meta:
        model = Document
        fields = ['document_id', 'doucment_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}
