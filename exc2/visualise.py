from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from numpy import arange, sin, cos, pi, exp
import numpy as np
import sys



# Define a plotting class
class Plot():
	def __init__(self):
		# initialise a dictionary to keep track of points (X,Y)
		self.traces = dict()

		# Setup the graph application and window
		self.app = QtGui.QApplication([])
		self.win = pg.GraphicsWindow(title='h_function')
		self.win.resize(800,450)
		self.win.setWindowTitle('h_function Plot')
		
		# Setup the scale
		self.canvas = self.win.addPlot(title='h(t)')

		# Setup the grid
		self.canvas.showGrid(x=True,y=True)

	# Start the application
	def start(self):
		# Check if it's on interactive mode or using pyside
		if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
			QtGui.QApplication.instance().exec()

	# Plot the existing points in the dictionary and append the new ones
	def trace(self, name, X_data, Y_data):
		if name in self.traces:
			self.traces[name].setData(X_data, Y_data)
		else:
			self.traces[name] = self.canvas.plot(pen='y')

# Define lambda function
def lambda_function(t_value):
	return 5*sin(2*pi*1*(t_value))

# Define h function
def h_function(t_value):
	return 3*pi*exp(lambda_function(t_value))

if __name__ == '__main__':
	plot = Plot()

	# Define a function that updates the plot
	def update_plot():
		global plot

		# h_function is periodic on integer values of t
		# arrange the value of time between periods
		t = np.arange(0,1.0,0.01)
		h_t = h_function(t)

		# Append the time and h(time) values to the plotting function
		plot.trace("h_t",t,h_t)

	# Initialise a timer with timeout duration of 40 msec
	timer = QtCore.QTimer()
	timer.timeout.connect(update_plot)
	timer.start(40)

	# Start the plot
	plot.start()