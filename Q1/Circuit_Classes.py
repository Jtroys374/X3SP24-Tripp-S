# region imports
from X2Q2_SP24 import doPlot, simulate
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from abc import ABC, abstractmethod
# these imports are necessary for drawing a matplot lib graph on my GUI
# no simple widget for this exists in QT Designer, so I have to add the widget in code.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure


# endregion

# region RLC circuit classes (MVC)
class circuitModel():
    def __init__(self):
        self.nodes = []
        self.resistors = []
        self.capacitors = []
        self.inductors = []
        self.voltageSources = []
        self.wires = []


class circuitView():
    def __init__(self, dw=None):
        if dw is not None:
            self.setDisplayWidgets(dw)
            self.setupImageLabel()
            self.setupPlot()

    def setDisplayWidgets(self, dw=None):
        if dw is not None:
            pass
            self.displayWidget = dw

    def setupImageLabel(self):
        """
        Displays picture of circuit from Circuit1.png in a label widget
        :return:
        """
        # region setup a label to display the image of the circuit
        self.pixMap = qtg.QPixmap()
        self.pixMap.load("Circuit1.png")
        self.image_label = qtw.QLabel()
        self.image_label.setPixmap(self.pixMap)
        self.layout_VertInput.addWidget(self.image_label)
        # endregion

    def setupPlot(self):
        """
        Create the figure, canvas, axes and toolbar objects and place them on GUI
        :return:
        """
        self.figure = Figure(figsize=(8, 8), tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot()
        self.toolbar = NavigationToolbar2QT(self.canvas, self.form)
        self.layout_VertMain.addWidget(self.toolbar)
        self.layout_VertMain.addWidget(self.canvas)

    def doPlot(self, args):
        self.canvas.figure.clear()
        self.ax = self.figure.add_subplot()
        doPlot(args, ax=self.ax)
        self.canvas.draw()


class circuitController():
    def __init__(self, args):
        """
        This is the class for a circuitContorller.  It has a model and view for the circuit.
        :param args: a tuple with input widgets and display widgets
        """
        self.inputWidgets, self.displayWidgets = args

        # unpack the input widgets
        self.inputWidgets

        self.Model = circuitModel()
        self.View = circuitView(dw=self.displayWidgets)

    def calculate(self):
        """
        Simulates the circuit by calling from X2Q1_SP22 functions.
        Step 1:  read inputs from GUI and clear figure.
        Step 2:  call simulate from import.
        Step 3:  call doPlot from import.
        :return:
        """
        L = float(self.inputWidgets.someLineEdit.text())
        R = float(self.inputWidgets.someLineEdit.text())
        C = float(self.inputWidgets.someLineEdit.text())
        A = float(self.inputWidgets.someLineEdit.text())
        f = float(self.inputWidgets.someLineEdit.text())
        p = float(self.inputWidgets.someLineEdit.text())
        t = float(self.inputWidgets.someLineEdit.text())
        pts = float(self.inputWidgets.someLineEdit.text())

        I = simulate(L, R, C, A, f, p, t, pts)
        self.View.doPlot((R, I.t, I))

# endregion
