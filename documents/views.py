from django.views.generic.detail import DetailView
from .models import Document, ArchObject, DigObject


class DocumentDetailView(DetailView):

    model = Document


class ArchObjectDetailView(DetailView):

    model = ArchObject

    def get_context_data(self, **kwargs):
        context = super(ArchObjectDetailView, self).get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(archobject__id=self.kwargs['pk'])
        return context


class DigObjectDetailView(DetailView):

    model = DigObject

    def get_context_data(self, **kwargs):
        context = super(DigObjectDetailView, self).get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(digobject__id=self.kwargs['pk'])
        return context
