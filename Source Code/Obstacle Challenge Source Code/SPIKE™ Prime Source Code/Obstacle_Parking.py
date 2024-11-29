from FE_Functions import *

def obstacleParking(robotDirection, recordListInput):
    
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)
    monke.start()

    hub.imu.reset_heading(0)

    try:
        i = 1
        headingTarget = 90 * robotDirection

        if ("Parking" not in recordListInput[i]):
            monke.driveMotor.control.limits(acceleration=800)
            monke.street(-100, 0, 2000, 2000)
            monke.look(0, False)
            monke.fastAcceleration(True)
            monke.street(-580, 0, 1000, 450)
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
                    monke.driveLine(1000, 2000, 2000, -12, -3)
                    monke.drive(100, 2000, 2000, -2, -1)
                    monke.turn(1, headingTarget + 80, 40, 2000, 2000)
                    monke.street(550, headingTarget + 80, 2000, 2000)
                    monke.turnSemi(1, headingTarget + 88, headingTarget + 90, 40, 2000, 2000)

                    i = (i + 1) % 4
                    headingTarget += 90

                monke.driveLine(1000, 2000, 2000, -12, -3)
                monke.street(200, headingTarget + 60, 900, 800)
                monke.streetStall(100, headingTarget, 800, 700, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-20, 0, 2000, 2000)
            monke.turn(-1, -92, 40, 850, 600)
            monke.look(RIGHT, False)
            monke.street(-100, -92, 500, 300)
            monke.HOLD(300)

            monke.fastAcceleration(False)
            monke.street(100, -90, 600, 700)
            monke.fastAcceleration(True)
            monke.streetStall(50, -90, 700, 900, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-100, 0, 2000, 2000)
            monke.fastAcceleration(True)



            # nParking CLOCKWISE
            monke.street(-850, -1, 2000, 2000)



            monke.street(-100, 0, 900, 800)
            monke.turn(-1, -92, 40, 800, 550)
            monke.streetStall(-200, -90, 600, 300, 1000)



        else:
            # COUNTERCLOCKWISE

            if ("Parking" not in recordListInput[i]):
                monke.turn(1, headingTarget + 3, 40, 2000, 2000)
                monke.drive(200, 2000, 2000, 15, 6)

                i += 1

                while ("Parking" not in recordListInput[i]):
                    monke.driveLine(1000, 2000, 2000, 12, 3)
                    monke.drive(100, 2000, 2000, 2, 1)
                    monke.turn(1, headingTarget - 80, 40, 2000, 2000)
                    monke.street(550, headingTarget - 80, 2000, 2000)
                    monke.turnSemi(1, headingTarget - 88, headingTarget - 90, 40, 2000, 2000)

                    i = (i + 1) % 4
                    headingTarget -= 90

                monke.driveLine(1000, 2000, 2000, 12, 3)
                monke.street(200, headingTarget - 60, 900, 800)
                monke.streetStall(100, headingTarget, 800, 700, 100)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-80, 0, 850, 800)
            monke.turn(-1, 92, 50, 850, 600)
            monke.look(LEFT, False)
            monke.street(-100, 92, 500, 300)
            monke.HOLD(300)

            monke.fastAcceleration(False)
            monke.streetStall(100, 90, 600, 650, 200)

            monke.driveMotor.control.limits(acceleration= 800)
            monke.street(-100, 0, 2000, 2000)
            monke.fastAcceleration(True)



            # fParking COUNTER
            monke.street(-1690, -1, 2000, 2000)



            monke.street(-100, 0, 900, 800)
            monke.turn(-1, 96, 40, 800, 600)
            monke.streetStall(-200, 88, 600, 300, 1000)

    finally:
        distanceSensor.lights.on(100)
        monke.look(90 * robotDirection, False)
        wait(500)

if __name__ == "__main__":
    print(f"\n\n\nVoltage: {hub.battery.voltage()}")
    hub.speaker.beep(500)

    recordListMain = [                                      # Start
                      ["Parking",  "---",      "Parking", "---"],
                      ["",  "---",      "", "---"], 
                      ["",  "---",      "", "---"], 
                      ["",  "---",      "", "---"]
                     ]

    obstacleParking(1, recordListMain)
    print(clock.time())
