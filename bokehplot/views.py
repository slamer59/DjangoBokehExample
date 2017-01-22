# Create your views here.
from django.shortcuts import render

from bokeh.embed import autoload_server


def simple_chart(request):
    # bokeh serve --allow-websocket-origin=127.0.0.1:8001 selection_histogram.py

    script = autoload_server(model=None,
                             app_path="/loadFileAndPlot",
                             url="http://localhost:5006/")

    return render(request, "simple_chart.html", {"the_script": script})
