#!/usr/bin/env python
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

#data is so odd 
data = [
	(1,111,222,333),
	(2,121,244,210),
	(3,131,252,112),
	(4,141,261,98),
		]

#do some change you can let show in an image 
drawing = Drawing(200,150)
one = [row[1]-80 for row in data]
two =  [row[2]-80 for row in data]
three =  [row[3]-80 for row in data]
time = [row[0]*10 for row in data]

drawing.add(PolyLine(zip(time,one),strokeColor=colors.blue))
drawing.add(PolyLine(zip(time,two),strokeColor=colors.red))
drawing.add(PolyLine(zip(time,three),strokeColor=colors.green))
drawing.add(String(65,115,'Sunspots',fontSize=18,fillColor=colors.red))

renderPDF.drawToFile(drawing,'report.pdf','Sunspots')
