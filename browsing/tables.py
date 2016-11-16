import django_tables2 as tables
from django_tables2.utils import A
from documents.models import Document, ArchObject, DigObject


class DocumentTable(tables.Table):
    document_id = tables.LinkColumn(
        'documents:document_detail', args=[A('pk')], verbose_name='URI')
    document_type = tables.Column(verbose_name='Document Type')

    class Meta:
        model = Document
        fields = ['document_id', 'document_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class ArchObjectTable(tables.Table):
    title = tables.LinkColumn(
        'documents:archobject_detail', args=[A('pk')], verbose_name='Title')
    object_type = tables.Column(verbose_name='Type')

    class Meta:
        model = ArchObject
        fields = ['title', 'object_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class DigObjectTable(tables.Table):
    title = tables.LinkColumn(
        'documents:digobject_detail', args=[A('pk')], verbose_name='Title')
    object_type = tables.Column(verbose_name='Type')
    attrs = {"class": "table table-hover table-striped table-condensed"}

    class Meta:
        model = DigObject
        fields = ['title', 'object_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}
