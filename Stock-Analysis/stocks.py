from pandas_datareader import data
import fix_yahoo_finance as yf 
import pandas
import datetime
from bokeh.plotting import figure, show, output_file


# Time Period
start = datetime.datetime(2017,6,1)
end = datetime.datetime(2018,6,1)

# Get data from yahoo
yf.pdr_override() 
df=data.get_data_yahoo(tickers="GOOG", start=start, end=end)

# Finds the appropriate value for the Status column
def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Close - df.Open)

# Create the Chart
p = figure(x_axis_type="datetime", width=1000, height=500)
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.5

hours_12 = 12*60*60*1000

# TODO: Add Hover tooltip to show the prices for each day

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
       hours_12, df.Height[df.Status == "Increase"],
       fill_color="#00CC33", line_color="black")
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
       hours_12, df.Height[df.Status == "Decrease"],
       fill_color="#FF3333", line_color="black")

output_file = "Stocks.html"
show(p)

