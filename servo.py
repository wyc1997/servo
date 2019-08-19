from multiprocessing import Process, Value
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import time

class Servo():
    def __init__(self, max_angle, turn_rate):
        '''
        Constructor accepts two parameters: 
        max_angle: the largest angle the servo is able to turn to
        turn_rate: unit: degree per 0.05s
        '''
        self.max_angle = max_angle
        self.turn_rate = turn_rate
        self.cur_angle = Value('d', 0)
    
    def getCurAngle(self):
        '''
        return the current angle, taking the minimum angle as 0
        '''
        return self.cur_angle.value

    def hold(self, position):
        '''
        takes 1 parameter:
        position: ranges from 0-1, where 0 stands for min angle, 1 stands for max angle, and 
        0.5 stands for neutral position
        '''
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
        time.sleep(0.05) 

    # helper function: can add parameters to plot different graphs (currently it is just angle 
    # vs time)
    # TODO: make the plot scrolling by changing the range of x axis
    #       fix an initial range
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
    
    # functions to start a sub-process to display the plot while allowing the main program to 
    # continue
    def plotAngleAgainstTime(self):
        p = Process(target=self.plotingUtilities)
        p.start()

        