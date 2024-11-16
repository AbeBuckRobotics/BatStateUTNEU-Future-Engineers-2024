from FE_Functions import *

def main():
    try:
        print(f"\n\nVoltage: {hub.battery.voltage()}")

        driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
        steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        colorSensor = ColorSensor(Port.D)
        distanceSensor = UltrasonicSensor(Port.C)

        monke = FutureEngineers(driveMotor, steerMotor, visionMotor)
        
        monke.driveMotor.control.limits(acceleration=800)

        openReady = 3
        proximityLeft = 0
        proximityRight = 0

        hub.imu.reset_heading(0)

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

        headingTarget = 0
        # proximityTarget = 600
        proximityTarget = 950
        robotDirection = 0
        robotLaps = 0
        driveMotorAngleTarget = 1500

        driveMotor.run(2000)

        errorSummation = 0
        errorPrevious = 0
        errorCorrection = 0
        streetErrorKp, streetErrorKi, streetErrorKd = 7, 0.0001, 3

        while True:
            errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKi, streetErrorKd, 1, errorSummation, errorPrevious)
            steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)

            csSat = intHSV(1)

            if (csSat > 30):
                csHueMax = 0

                while (csSat > 15):
                    csHueMax = max(intHSV(0), csHueMax)
                    csSat = intHSV(1)

                if (csHueMax > 190 and csHueMax < 290):
                    robotDirection = -1
                else:
                    robotDirection = 1

                break

        print(f"Direction: {robotDirection}")
        driveMotorAnglePrevious = driveMotor.angle()

        while (robotLaps < 3):
            if (robotLaps != 0):
                visionMotorAngleTarget = -90 * robotDirection * -1
                driveMotorAngleDeterminator = True

                errorSummation = 0
                errorPrevious = 0
                errorCorrection = 0

                while (distanceSensor.distance() < 1600 or driveMotorAngleDeterminator):
                    errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKi, streetErrorKd, 1, errorSummation, errorPrevious)
                    visionMotor.track_target(headingTarget - hub.imu.heading() + visionMotorAngleTarget)
                    steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)

                    if ((driveMotor.angle() - driveMotorAnglePrevious) > driveMotorAngleTarget):
                        hub.speaker.beep(500)
                        driveMotorAngleDeterminator = False

            print(f"Travel: {driveMotor.angle() - driveMotorAnglePrevious}\t\t\b\b\bLaps: {robotLaps + 0.25}")
            driveMotorAnglePrevious = driveMotor.angle()

            errorSummation = 0
            errorPrevious = 0
            errorCorrection = 0

            while (abs(hub.imu.heading()) < abs(headingTarget) + 90):
                vmCorrection = headingTarget - hub.imu.heading()
                errorSummation, errorPrevious, errorCorrection = pid(headingTarget + 90 * robotDirection - hub.imu.heading(), 2, 0.0001, 0.3, 1, errorSummation, errorPrevious)
                
                errorCorrection = min(errorCorrection, 40) if (errorCorrection > 0) else max(errorCorrection, -40)
                steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)
                visionMotor.track_target(vmCorrection * -1)

            robotLaps += 0.25
            headingTarget += 90 * robotDirection

            if (robotDirection < 0):
                headingTarget -= 0.3
            else:
                headingTarget += 0.3

        errorSummation = 0
        errorPrevious = 0
        errorCorrection = 0
        driveMotorAnglePrevious = driveMotor.angle()

        while (driveMotor.angle() < driveMotorAnglePrevious + 700):
            errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKi, streetErrorKd, 1, errorSummation, errorPrevious)
            visionMotor.track_target(headingTarget - hub.imu.heading() + visionMotorAngleTarget)
            steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)

        driveMotor.hold()

    finally:
        print(f"\nTime: {clock.time()}")

if __name__ == "__main__":
    main()