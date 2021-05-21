""" import matplotlib
matplotlib.use(‘TkAgg’)
import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()   """

import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([item1, item2])