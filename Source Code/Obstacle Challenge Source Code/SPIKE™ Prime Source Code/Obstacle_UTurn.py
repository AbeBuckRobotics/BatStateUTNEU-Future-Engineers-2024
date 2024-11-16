from FE_Functions import *

def obstacleUTurn(recordListInput, robotDirection):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    try:
        if (True):
            # UTURN

            print("UTURN")

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-50, 0, 2000, 2000)
            monke.fastAcceleration(True)
            monke.street(-500, 0, 2000, 2000)
            monke.street(-300, 0, 700, 350)
            monke.HOLD(100)

            if (robotDirection == 1):
                # UTURN CLOCKWISE

                monke.fastAcceleration(False)
                monke.street(10, 0, 800, 800)
                monke.look(LEFT, False)
                monke.fastAcceleration(True)
                monke.turn(1, -90, 40, 900, 700)
                monke.streetStall(1, -90, 2000, 2000, 250)

            else:
                # UTURN COUNTERCLOCKWISE

                monke.fastAcceleration(False)
                monke.street(150, 0, 2000, 2000)
                monke.look(RIGHT, False)
                monke.fastAcceleration(True)
                monke.turn(1, 90, 40, 1500, 700)
                monke.streetStall(1, 90, 2000, 2000, 100)

        else:
            # NO UTURN

            print("NO UTURN")

    finally:
        monke.motorClose()

if __name__ == "__main__":
    try:
        robotDirection = 1
        obstacleUTurn([], robotDirection)

        while True: pass

    finally:
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        s.run_target(1000, 0, Stop.HOLD, False)
        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

        if (robotDirection == 1):
            v.run_target(1000, RIGHT, Stop.HOLD, False)
        else:
            v.run_target(1000, LEFT, Stop.HOLD, False)

        wait(800)
