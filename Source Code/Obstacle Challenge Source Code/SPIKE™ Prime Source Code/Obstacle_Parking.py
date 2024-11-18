from FE_Functions import *

def obstacleParking(robotDirection, recordListInput):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    hub.imu.reset_heading(0)

    try:
        i = 1
        headingTarget = 90 * robotDirection

        if ("Parking" not in recordListInput[i]):
            monke.driveMotor.control.limits(acceleration=800)
            monke.street(-100, 0, 2000, 2000)
            monke.look(0, False)
            monke.fastAcceleration(True)
            monke.street(-610, 0, 1000, 450)
            monke.HOLD(100)

            monke.fastAcceleration(False)
            monke.street(100, 0, 2000, 2000)
            monke.fastAcceleration(True)
            monke.street(200, 0, 2000, 2000)

        if (robotDirection == 1): 
            # CLOCKWISE

            if ("Parking" not in recordListInput[i]):
                monke.turn(1, headingTarget - 3, 40, 2000, 2000)
                monke.drive(600, 2000, 2000, -15, -6)

                i += 1

                while ("Parking" not in recordListInput[i]):
                    monke.driveLine(1200, 2000, 2000, -12, -3)
                    monke.turn(1, headingTarget + 80, 40, 2000, 2000)
                    monke.streetLine(1, headingTarget + 80, 2000, 2000)
                    monke.street(550, headingTarget + 80, 2000, 2000)
                    monke.turn(1, headingTarget + 88, 40, 2000, 2000)

                    i = (i + 1) % 4
                    headingTarget += 90

                monke.drive(1100, 2000, 2000, -12, -3)
                monke.street(700, headingTarget + 40, 2000, 2000)
                monke.look(RIGHT, False)
                monke.streetStall(400, headingTarget, 800, 700, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-20, 0, 2000, 2000)
            monke.turn(-1, -92, 40, 850, 600)
            monke.look(RIGHT, False)
            monke.street(-100, -92, 500, 300)
            monke.HOLD(100)

            monke.fastAcceleration(False)
            monke.street(150, -90, 2000, 2000)
            monke.fastAcceleration(True)
            monke.streetStall(100, -90, 2000, 2000, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-100, 0, 2000, 2000)
            monke.fastAcceleration(True)

            if (recordListInput[i][0] == "Parking"):
                # nParking
                monke.street(-680, -1, 2000, 2000)

            elif (recordListInput[i][2] == "Parking"):
                # fParking
                monke.street(-1630, -1, 2000, 2000)

            monke.street(-100, 0, 900, 800)
            monke.turn(-1, -92, 40, 800, 550)
            monke.streetStall(-120, -90, 700, 900, 100)



        else:
            # COUNTERCLOCKWISE

            if ("Parking" not in recordListInput[i]):
                monke.turn(1, headingTarget + 3, 40, 2000, 2000)
                monke.drive(200, 2000, 2000, 15, 6)

                i += 1

                while ("Parking" not in recordListInput[i]):
                    monke.driveLine(1200, 2000, 2000, 12, 3)
                    monke.turn(1, headingTarget - 80, 40, 2000, 2000)
                    monke.streetLine(1, headingTarget - 80, 2000, 2000)
                    monke.street(550, headingTarget - 80, 2000, 2000)
                    monke.turn(1, headingTarget - 88, 40, 2000, 2000)

                    i = (i + 1) % 4
                    headingTarget -= 90

                monke.drive(1300, 2000, 2000, 12, 3)
                monke.street(700, headingTarget - 40, 2000, 2000)
                monke.look(LEFT, False)
                monke.streetStall(400, headingTarget, 800, 700, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-10, 0, 2000, 2000)
            monke.turn(-1, 92, 50, 850, 600)
            monke.look(LEFT, False)
            monke.street(-100, 92, 500, 300)
            monke.HOLD(100)

            monke.fastAcceleration(False)
            monke.street(150, 90, 2000, 2000)
            monke.fastAcceleration(True)
            monke.streetStall(220, 90, 2000, 2000, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-100, 0, 2000, 2000)
            monke.fastAcceleration(True)

            if (recordListInput[i][0] == "Parking"):
                # nParking
                monke.street(-720, -1, 2000, 2000)

            elif (recordListInput[i][2] == "Parking"):
                # fParking
                monke.street(-1650, -1, 2000, 2000)

            monke.turnStall(-1, 89, 90, 40, 2000, 2000, 200)

    finally:
        distanceSensor.lights.on(100)
        monke.look(90 * robotDirection, False)
        wait(500)

if __name__ == "__main__":
    print(f"\n\n\nVoltage: {hub.battery.voltage()}")
    hub.speaker.beep(500)

    recordListMain = [["", "---", "", "---"],   # Start
                      ["", "---", "Parking", "---"], 
                      ["", "---", "", "---"], 
                      ["", "---", "", "---"]]

    obstacleParking(1, recordListMain)
    print(clock.time())
