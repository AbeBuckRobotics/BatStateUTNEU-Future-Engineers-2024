from FE_Functions import *

def obstacleParking(robotDirection, recordListInput):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    hub.imu.reset_heading(0)

    if (robotDirection == 1): 
        # CLOCKWISE

        try:
            i = 1
            headingTarget = 90

            if ("Parking" not in recordListInput[i]):
                monke.driveMotor.control.limits(acceleration=800)
                monke.street(-150, 0, 2000, 2000)
                monke.look(0, False)
                monke.fastAcceleration(True)
                monke.street(-560, 0, 1000, 450)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(230, 0, 2000, 2000)
                monke.look(0, False)
                monke.turn(1, headingTarget - 3, 40, 2000, 2000)
                monke.drive(600, 2000, 2000, -15, -6)

                i += 1

                while ("Parking" not in recordListInput[i]):
                    monke.driveLine(1200, 2000, 2000, -12, -3)
                    monke.turn(1, headingTarget + 80, 40, 2000, 2000)
                    monke.street(600, headingTarget + 80, 2000, 2000)
                    monke.turn(1, headingTarget + 88, 40, 2000, 2000)

                    i = (i + 1) % 4
                    headingTarget += 90

                monke.drive(1100, 2000, 2000, -12, -3)
                monke.street(700, headingTarget + 40, 2000, 2000)
                monke.look(90, False)
                monke.streetStall(300, headingTarget, 800, 600, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-20, 0, 2000, 2000)
            monke.turn(-1, 90, 40, 2000, 2000)
            monke.look(0, False)
            monke.streetStall(-10, 90, 2000, 500, 200)
            monke.fastAcceleration(False)
            monke.street(100, 0, 2000, 2000)
            monke.fastAcceleration(True)

            if (recordListInput[i][0] == "Parking"):
                # nParking
                monke.street(820, -2, 2000, 2000)

            elif (recordListInput[i][2] == "Parking"):
                # fParking
                monke.street(1730, -2, 2000, 2000)

            monke.look(90, False)
            monke.turnStall(1, -70, -90, 40, 2000, 2000, 200)

        finally:
            monke.look(90, False)
            wait(500)

    else:
        # COUNTERCLOCKWISE

        pass

if __name__ == "__main__":
    print(hub.battery.voltage())
    hub.speaker.beep(500)

    recordListMain = [["Parking", "---", "", "---"], ["", "---", "", "---"], ["", "---", "", "---"], ["", "---", "", "---"]]

    obstacleParking(1, recordListMain)
    print(clock.time())
