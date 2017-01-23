from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import AjaxDataSource
from bokeh.plotting import figure

source = AjaxDataSource(data=dict(x=[], y=[]),
                        data_url='http://localhost:8001/upload/list/documents/2017/01/23/data.csv',
                        polling_interval=100)
p = figure()
p.circle('x', 'y', source=source)

p.x_range.follow = "end"
p.x_range.follow_interval = 10

# desc.on_change('userInput', update_data)

sizing_mode = 'fixed'  # 'scale_width' also looks nice with this example
l = layout([
    [p],
], sizing_mode=sizing_mode)

curdoc().add_root(l)
