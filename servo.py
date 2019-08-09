from multiprocessing import Process
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

class Servo():
    def __init__(self, max_angle, turn_rate):
        self.max_angle = max_angle
        self.turn_rate = turn_rate
        self.cur_angle = 0
    
    def getCurAngle(self):
        return self.cur_angle

    def hold(self, position):
        if position > 1 or position < 0:
            return "invalid input: must range from 0 to 1"
        target_angle = position * self.max_angle
        delta_angle = target_angle - self.cur_angle
        if delta_angle > 0:
            if delta_angle > self.turn_rate:
                self.cur_angle += self.turn_rate
            else:
                self.cur_angle += delta_angle
        else:
            if delta_angle < -1 * self.turn_rate:
                self.cur_angle -= self.turn_rate
            else:
                self.cur_angle -= delta_angle

    def plotAngleAgainstTime(self):
        app = QtGui.QApplication([])

        win = pg.GraphicsWindow(title="Angle vs. Time")
        plt = win.addPlot(title="Current angle")
        curve = plt.plot(pen="y")
        data=[]
        def update():
            data.append(self.getCurAngle())
            curve.setData(data)
        timer = QtCore.QTimer()
        timer.timeout.connect(update)
        timer.start(50)
        QtGui.QApplication.instance().exec_()
<<<<<<< HEAD
    
    # TODO: shared variable 
=======
#this is a branch test
>>>>>>> test
    def plot(self):
        p = Process(target=self.plotAngleAgainstTime)
        p.start()

        

def main():
    s = Servo(180, 0.001)
    while True:
        s.hold(1)
        print(s.getCurAngle())

if __name__ == "__main__":
    main()