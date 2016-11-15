from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
# from editions.models import Edition, Period
from documents.models import Document
from collections import Counter
from vocabs.models import SkosConcept

DATA = {"status": "ok",
        "query": "api:graph",
        "timestamp": "2016-07-21T09:56:36.803Z",
        "items": "7",
        "title": "LASK4EVER",
        "subtitle": "This is just a test to check if everythin works as expected.",
        "legendx": "Club",
        "legendy": "# of Victories",
        "measuredObject": "Victories",
        "ymin": -10,
        "payload": [
            ["Club", "# of Victories"],
            ["LASK", 10],
            ["Real Madrid", 4],
            ["Rapid Wien", 0],
            ["Blau Weiß Linz", -10]
        ]
        }

DATA_PIECHART = {
    "items": "2",
    "title": "LASK4EVER",
    "subtitle": "This is just a test.",
    "measuredObject": "# of Victories",
    "payload": [
        ["LASK", 9], ["Blau Weiß Linz", 1]
    ]
}


def barcharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/bar_charts.html', context)


def piecharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/pie_charts.html', context)


def documenttype_json(request):
    documents = Document.objects.values(
        'document_type').annotate(total=Count('document_type')).order_by('-total')
    payload = []
    for x in documents:
        temp_doc_type = SkosConcept.objects.get(id=int(x['document_type']))
        entry = [temp_doc_type.pref_label, x['total']]
        payload.append(entry)

        data = {"items": len(Document.objects.all()),
                "title": "Documents and their types",
                "subtitle": "Documents and their types",
                "legendx": "Types",
                "legendy": "Number of Documents",
                "measuredObject": "Documents",
                "payload": payload
                }
    return JsonResponse(data)


def test_json(request):
    data = DATA
    return JsonResponse(data)


def test_json_pie(request):
    data = DATA_PIECHART
    return JsonResponse(data)
