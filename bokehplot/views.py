# Create your views here.
import csv
import json
from django.http import JsonResponse
from django.shortcuts import render

import bokeh
import numpy as np
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


def sliders(request):
    # session = bokeh.client.pull_session(app_path="/sliders",
    #                          url="http://localhost:5006/")
    session = bokeh.client.pull_session(session_id=None, url='http://localhost:5006/sliders/')
    source = session.document.get_model_by_name('source')
    # Get the current slider values
    a = 2
    b = 1.7
    w = 0
    k = 1
    N = 10
    # Generate the new curve
    x = np.linspace(0, 4 * np.pi, N)
    y = a * np.sin(k * x + w) + b

    source.data = dict(x=x, y=y)

    script = autoload_server(None, app_path='/sliders', session_id=session.id)
    # update_document(doc, request)
    # script = autoload_server(model=None,
    #                          app_path="/sliders",
    #                          url="http://localhost:5006/"
    #                          )

    return render(request, "simple_chart.html", {"the_script": script})
