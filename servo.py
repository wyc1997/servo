class Servo():
    def __init__(self, max_angle, turn_rate):
        self.max_angle = max_angle
        self.turn_rate = turn_rate
        self.cur_angle = 0
    
    def getCurAngle(self):
        return self.cur_angle

    def hold(self, position):
        