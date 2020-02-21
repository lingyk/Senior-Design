from tkinter import *
from tkinter.ttk import *

def create_circle(x, y, r, canvasName,**kwags): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,**kwags)

def create_text(x,y,canvasName, **kwags):
    return canvasName.create_text(x,y,**kwags)

def round_rectangle(canvasName, x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvasName.create_polygon(points, **kwargs, smooth=True)



