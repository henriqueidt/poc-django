from django.http import HttpResponse
from django.shortcuts import render


def templateTest(response):
    return render(response, "templateTest.html", {
        "list": [
            {
                "name": "Ford",
                "count": 12
            },
            {
                "name": "Chevy",
                "count": 1
            },
            {
                "name": "BMW",
                "count": 0 
            }
        ]
    })
