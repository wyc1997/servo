from servo import Servo

def main():
    s = Servo(180, 1)
    s.plotAngleAgainstTime()
    while True:
        print(s.getCurAngle())
        s.hold(1)

if __name__ == '__main__':
    main()
    