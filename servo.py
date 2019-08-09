from multiprocessing import Process, Value
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

class Servo():
    def __init__(self, max_angle, turn_rate):
        self.max_angle = max_angle
        self.turn_rate = turn_rate
        self.cur_angle = Value('d', 0)
    
    def getCurAngle(self):
        return self.cur_angle.value

    def hold(self, position):
        if position > 1 or position < 0:
            return "invalid input: must range from 0 to 1"
        target_angle = position * self.max_angle
        delta_angle = target_angle - self.cur_angle.value
        if delta_angle > 0:
            if delta_angle > self.turn_rate:
                self.cur_angle.value += self.turn_rate
            else:
                self.cur_angle.value += delta_angle
        else:
            if delta_angle < -1 * self.turn_rate:
                self.cur_angle.value -= self.turn_rate
            else:
                self.cur_angle.value -= delta_angle

    def plotingUtilities(self):
        app = QtGui.QApplication([])

        win = pg.GraphicsWindow(title="Angle vs. Time")
        plt = win.addPlot(title="Current angle")
        curve = plt.plot(pen="y")
        plt.setYRange(0, self.max_angle)
        data=[]
        ptr=0
        def update():
            # nonlocal ptr
            # ptr+=1
            data.append(self.cur_angle.value)
            curve.setData(data)
            # curve.setPos(ptr, 0)
        timer = QtCore.QTimer()
        timer.timeout.connect(update)
        timer.start(100)
        QtGui.QApplication.instance().exec_()
    
    # TODO: shared variable 
    def plotAngleAgainstTime(self):
        p = Process(target=self.plotingUtilities)
        p.start()

        

def main():
    s = Servo(180, 0.001)
    while True:
        s.hold(1)
        print(s.getCurAngle())

if __name__ == "__main__":
    main()