from django.db import models
from vocabs.models import SkosConcept


class Areal(models.Model):
    name = models.CharField(max_length=300)


class Planquadrat(models.Model):
    name = models.CharField(max_length=300)


class Planum(models.Model):
    name = models.CharField(max_length=300)


class ArchObject(models.Model):
    title = models.CharField(max_length=300)
    object_type = models.ForeignKey(SkosConcept)


class DigObject(models.Model):
    title = models.CharField(max_length=300)
    object_type = models.ForeignKey(SkosConcept)


class Document(models.Model):

    """Holds information about documents. (cidoc:E31)"""
    document_id = models.URLField(unique=True)
    document_filename = models.CharField(max_length=300, unique=True)
    document_name = models.CharField(max_length=300, unique=True)
    doucment_type = models.ForeignKey(SkosConcept)
    areal = models.ForeignKey(Areal)
    planquadrat = models.ForeignKey(Planquadrat)
    planum = models.ForeignKey(Planum)
    archobject = models.ManyToManyField(ArchObject, blank=True)
    DigObject = models.ManyToManyField(DigObject, blank=True)

    def __str__(self):
        return "{}".format(self.document_id)
