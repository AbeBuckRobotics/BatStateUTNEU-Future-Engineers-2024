from FE_Functions import *

def main():
    try:
        print(f"\n\nVoltage: {hub.battery.voltage()}")

        driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
        steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

        monke = FutureEngineers(driveMotor, steerMotor, visionMotor)
        monke.start()
        
        monke.driveMotor.control.limits(acceleration= 800)

        openReady = 3
        proximityLeft = 0
        proximityRight = 0
        headingTarget = 0
        robotDirection = 0
        robotLaps = 0

        # checkpoint

        robotSpeed = const(1000)
        robotTurn = const(90)
        proximityTarget = const(500)
        driveMotorAngleTarget = 1800
        
        streetErrorKpMax = const(7)
        streetErrorKiMax = const(0.000)
        streetErrorKdMax = const(3)

        turnErrorKpMax = const(2)
        turnErrorKiMax = const(0.0001)
        turnErrorKdMax = const(0.3)

        hub.imu.reset_heading(0)

        wait(500)

        while (openReady):
            steerMotor.run_target(1000, 0, Stop.HOLD, False)

            if (openReady == 3):
                visionMotor.run_target(1000, -95, Stop.HOLD, False)
                if (visionMotor.angle() <= -88):
                    wait(100)
                    proximityLeft = distanceSensor.distance()
                    openReady -= 1
            
            elif (openReady == 2):
                visionMotor.run_target(1000, 95, Stop.HOLD, False)
                if (visionMotor.angle() >= 88):
                    wait(100)
                    proximityRight = distanceSensor.distance()
                    openReady -= 1

            else: 
                visionMotor.run_target(1000, 0, Stop.HOLD, False)
                if (visionMotor.angle() <= 5):
                    wait(100)
                    openReady -= 1
                    
        print(f"Left: {proximityLeft}\tRight: {proximityRight}")

        robotDirection = monke.streetDetermineTheLine(10, 0, robotSpeed, robotSpeed)

        errorSummation = 0
        errorPrevious = 0
        errorCorrection = 0

        while (distanceSensor.distance() > proximityTarget):
            streetErrorKp = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKpMax)
            streetErrorKd = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKdMax)
            errorSummation, errorPrevious, errorCorrection = pid(0 - hub.imu.heading(), streetErrorKp, streetErrorKiMax, streetErrorKd, 1, errorSummation, errorPrevious)

            monke.move(robotSpeed, errorCorrection)

        print(f"Direction: {robotDirection}")
        driveMotorAnglePrevious = driveMotor.angle()

        while (robotLaps < 3):
            if (robotLaps != 0):
                visionMotorAngleTarget = -90 * robotDirection
                driveMotorAngleDeterminator = True

                errorSummation = 0
                errorPrevious = 0
                errorCorrection = 0

                while (distanceSensor.distance() > proximityTarget or driveMotorAngleDeterminator):
                    streetErrorKp = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKpMax)
                    streetErrorKd = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKdMax)
                    errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKiMax, streetErrorKd, 1, errorSummation, errorPrevious)
                    visionMotor.track_target(headingTarget - hub.imu.heading() + visionMotorAngleTarget)

                    if ((driveMotor.angle() - driveMotorAnglePrevious) > driveMotorAngleTarget - 250):
                        visionMotorAngleTarget = 0
                    if ((driveMotor.angle() - driveMotorAnglePrevious) > driveMotorAngleTarget):
                        hub.speaker.beep(500)
                        driveMotorAngleDeterminator = False

                    monke.move(robotSpeed, errorCorrection)

                driveMotorAngleTarget = 2300

            print(f"Travel: {driveMotor.angle() - driveMotorAnglePrevious}\t\t\b\b\bLaps: {robotLaps + 0.25}")
            driveMotorAnglePrevious = driveMotor.angle()

            errorSummation = 0
            errorPrevious = 0
            errorCorrection = 0

            while (abs(hub.imu.heading()) < abs(headingTarget) + robotTurn):
                turnErrorKp = linearMap(monke.driveMotor.speed(), 0, 1000, 0, turnErrorKpMax)
                turnErrorKd = linearMap(monke.driveMotor.speed(), 0, 1000, 0, turnErrorKdMax)
                vmCorrection = headingTarget - hub.imu.heading()
                errorSummation, errorPrevious, errorCorrection = pid(headingTarget + robotTurn * robotDirection - hub.imu.heading(), turnErrorKp, turnErrorKiMax, turnErrorKd, 1, errorSummation, errorPrevious)
                
                errorCorrection = min(errorCorrection, 40) if (errorCorrection > 0) else max(errorCorrection, -40)
                visionMotor.track_target(vmCorrection)

                monke.move(robotSpeed, errorCorrection)

            robotLaps += 0.25
            headingTarget += 90 * robotDirection

            if (robotDirection > 0):
                # CLOCKWISE
                # pos = inner
                # neg = outer
                headingTarget += -0.3 
            else:
                # COUNTERCLOCKWISE
                # pos = inner
                # neg = outer
                headingTarget -= 0.55

        errorSummation = 0
        errorPrevious = 0
        errorCorrection = 0
        driveMotorAnglePrevious = driveMotor.angle()

        while (driveMotor.angle() < driveMotorAnglePrevious + 500 or distanceSensor.distance() > 1300):
            streetErrorKp = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKpMax)
            streetErrorKd = linearMap(monke.driveMotor.speed(), 0, 1000, 0, streetErrorKdMax)
            errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKiMax, streetErrorKd, 1, errorSummation, errorPrevious)
            visionMotor.track_target(headingTarget - hub.imu.heading())
            
            monke.move(robotSpeed, errorCorrection)

        monke.HOLD(500)

    finally:
        print(f"\nTime: {clock.time()}")

if __name__ == "__main__":
    main()


