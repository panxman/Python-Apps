from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource


df["Start_formatted"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_formatted"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
source = ColumnDataSource(df)

# Create Figure
p = figure(x_axis_type='datetime', height=150, width=800,
           title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

# Create hover Tooltip
hover = HoverTool(tooltips=[("Start", "@Start_formatted"),
                            ("End",   "@End_formatted")])
p.add_tools(hover)

# Create the squares
p.quad(left="Start", right="End", bottom=0, top=1,
       color="green", source=source)

output_file("Graph.html")
show(p)
