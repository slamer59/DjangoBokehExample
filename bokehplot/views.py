# Create your views here.
import csv
import json
from django.http import JsonResponse
from django.shortcuts import render

import pandas as pandas
from bokeh.embed import autoload_server


def simple_chart(request):
    # bokeh serve --allow-websocket-origin=127.0.0.1:8001 selection_histogram.py

    script = autoload_server(model=None,
                             app_path="/loadFileAndPlot",
                             url="http://localhost:5006/")

    return render(request, "simple_chart.html", {"the_script": script})


def get_json(request):
    csv_filename = 'BokehApp/data-1.csv'
    # https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv
    csvFile = pandas.read_csv(filepath_or_buffer=csv_filename, sep=";")
    # with open(csv_filename, 'r') as csvfile:
    #     csv_reader = csv.DictReader(csvfile)

    return JsonResponse(csvFile.to_json(), safe=False)


def get_csv(request):
    csv_filename = request.path[13:]
    # https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv
    # csvFile = pandas.read_csv(filepath_or_buffer=csv_filename, sep=";")
    with open(csv_filename) as f:
        reader = csv.DictReader(f, delimiter=';')
        rows = list(reader)
    rows = {'x': [0.0, 1.0, 20.0], 'y': [0.0, 1.0, 20.0]}
    return JsonResponse(json.dumps(rows), safe=False)


def stocks(request):
    # bokeh serve --allow-websocket-origin=127.0.0.1:8001 selection_histogram.py

    script = autoload_server(model=None,
                             app_path="/stockMain",
                             url="http://localhost:5006/")

    return render(request, "simple_chart.html", {"the_script": script})


def ajaxSource(request):
    # bokeh serve --allow-websocket-origin=127.0.0.1:8001 selection_histogram.py

    script = autoload_server(model=None,
                             app_path="/remoteSourcePlot",
                             url="http://localhost:5006/")

    return render(request, "simple_chart.html", {"the_script": script})
