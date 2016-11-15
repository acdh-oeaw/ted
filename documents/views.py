from django.views.generic.detail import DetailView
from .models import Document


class DocumentDetailView(DetailView):

    model = Document
