import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource, Div
from bokeh.plotting import Figure

desc = Div(text="""
<h1>A simple example</h1>

<form action="#" method="get">
 <input type=file name="mytextbox" size="1"/>
 <input type="submit" class="btn" value="Click" name="mybtn">
</form>


<br />""", width=800)

# Create Column Data Source that will be used by the plot
source = ColumnDataSource(data=dict(x=[], y=[]))

p = Figure(plot_height=550, plot_width=800, title="", toolbar_location='above')
p.line(x="x", y="y", source=source)


def update_data():
    dataCSV = np.genfromtxt('data.csv', delimiter=';', names=['x', 'y'])  # function to read specific file type
    source.data = dict(
        x=dataCSV['x'],
        y=dataCSV['y'],
    )


# desc.on_change('userInput', update_data)

sizing_mode = 'fixed'  # 'scale_width' also looks nice with this example
l = layout([
    [desc],
    [p],
], sizing_mode=sizing_mode)
update_data()
curdoc().add_root(l)
