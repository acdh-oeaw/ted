from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept


class Areal(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Planquadrat(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Planum(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ArchObject(models.Model):
    title = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.object_type)


class DigObject(models.Model):
    title = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.object_type)


class Document(models.Model):

    """Holds information about documents. (cidoc:E31)"""
    document_id = models.URLField(blank=True)
    document_filename = models.CharField(max_length=300, blank=True)
    document_name = models.CharField(max_length=300, blank=True)
    doucment_type = models.ForeignKey(SkosConcept, blank=True, null=True)
    areal = models.ForeignKey(Areal, null=True, blank=True)
    planquadrat = models.ForeignKey(Planquadrat, blank=True, null=True)
    planum = models.ForeignKey(Planum, blank=True, null=True)
    archobject = models.ManyToManyField(ArchObject, blank=True)
    digobject = models.ManyToManyField(DigObject, blank=True)

    def __str__(self):
        return "{}".format(self.document_id)

    def get_absolute_url(self):
        return reverse('documents:document_detail', kwargs={'pk': self.id})
