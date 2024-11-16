from FE_Functions import *

def main():
    hub = PrimeHub()
    timer = StopWatch()

    try:
        hub.system.set_stop_button([Button.BLUETOOTH])
        hub.speaker.volume(100)
        hub.display.off()
        hub.light.off()

        driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
        steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        visionMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE, [1], False, 5)
        colorSensor = ColorSensor(Port.D)
        distanceSensor = UltrasonicSensor(Port.C)

        steerMotor.control.pid(ki=93464, integral_deadzone= 8, integral_rate=2000)

        monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

        driveMotor.control.limits(2000, 2000, 1000)
        steerMotor.control.limits(2000, 20000, 1000)
        visionMotor.control.limits(2000, 20000, 1000)

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
        proximityTarget = 900
        robotDirection = 0
        robotLaps = 0
        driveMotorAngleTarget = 1900

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
                visionMotorAngleTarget = -90 * robotDirection
                driveMotorAngleDeterminator = True

                errorSummation = 0
                errorPrevious = 0
                errorCorrection = 0

                while (distanceSensor.distance() > proximityTarget or driveMotorAngleDeterminator):
                    errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKi, streetErrorKd, 1, errorSummation, errorPrevious)
                    visionMotor.track_target(headingTarget - hub.imu.heading() + visionMotorAngleTarget)
                    steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)

                    if ((driveMotor.angle() - driveMotorAnglePrevious) > driveMotorAngleTarget - 250):
                        visionMotorAngleTarget = 0
                    if ((driveMotor.angle() - driveMotorAnglePrevious) > driveMotorAngleTarget):
                        hub.speaker.beep(500)
                        driveMotorAngleDeterminator = False

                driveMotorAngleTarget = 2300

            print(f"Travel: {driveMotor.angle() - driveMotorAnglePrevious}\t\t\b\b\bLaps: {robotLaps + 0.25}")
            driveMotorAnglePrevious = driveMotor.angle()

            errorSummation = 0
            errorPrevious = 0
            errorCorrection = 0

            while (abs(hub.imu.heading()) < abs(headingTarget) + 90):
                vmCorrection = headingTarget - hub.imu.heading()
                errorSummation, errorPrevious, errorCorrection = pid(headingTarget + 90 * robotDirection - hub.imu.heading(), 2, 0.0001, 0.3, 1, errorSummation, errorPrevious)
                
                errorCorrection = min(errorCorrection, 30) if (errorCorrection > 0) else max(errorCorrection, -30)
                steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)
                visionMotor.track_target(vmCorrection)

            robotLaps += 0.25
            headingTarget += 90 * robotDirection

            if (robotDirection < 0):
                headingTarget += 0
            else:
                headingTarget += 0.3

        errorSummation = 0
        errorPrevious = 0
        errorCorrection = 0
        driveMotorAnglePrevious = driveMotor.angle()

        while (driveMotor.angle() < driveMotorAnglePrevious + 800):
            errorSummation, errorPrevious, errorCorrection = pid(headingTarget - hub.imu.heading(), streetErrorKp, streetErrorKi, streetErrorKd, 1, errorSummation, errorPrevious)
            visionMotor.track_target(headingTarget - hub.imu.heading() + visionMotorAngleTarget)
            steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False)

        driveMotor.hold()

    finally:
        print(f"\nTime: {timer.time()}")

if __name__ == "__main__":
    main()