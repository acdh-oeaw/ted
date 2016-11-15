import django_tables2 as tables
# from django_tables2.utils import A
from documents.models import Document


class DocumentTable(tables.Table):
    id = tables.Column(verbose_name='ID')
    # document_id = tables.LinkColumn(
    #     'documents:document_detail', args=[A('pk')], verbose_name='Document')
    document_id = tables.Column(verbose_name='URI')

    class Meta:
        model = Document
        fields = ['id', 'document_id']
        attrs = {"class": "table table-hover table-striped table-condensed"}
