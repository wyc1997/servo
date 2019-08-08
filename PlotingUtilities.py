from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from servo import Servo


def plotAngleAgainstTime(s):
    app = QtGui.QApplication([])

    win = pg.GraphicsWindow(title="Servo angle against Time")

    pg.setConfigOptions(antialias=True)
    p6 = win.addPlot(title="Updating plot")
    curve = p6.plot(pen='y')
    data = []
    def update():
        data.append(s.getCurAngle())
        curve.setData(data)
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
    QtGui.QApplication.instance().exec_()

def main():
    s = Servo(180, 0.001)
    s.plot()
    while True:
        print(s.getCurAngle())
        s.hold(1)


if __name__ == '__main__':
    main()
    