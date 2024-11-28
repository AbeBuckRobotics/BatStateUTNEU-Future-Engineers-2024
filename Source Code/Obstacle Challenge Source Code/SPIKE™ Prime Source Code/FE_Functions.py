from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Icon, Port, Side, Stop
from pybricks.tools import StopWatch, wait
from micropython import const
from pupremote_hub import PUPRemoteHub

LEFT, RIGHT = const(-90), const(90)

hub = PrimeHub()
clock = StopWatch()

hub.system.set_stop_button([Button.BLUETOOTH])
hub.speaker.volume(100)
hub.display.off()
hub.light.off()

colorSensor = ColorSensor(Port.D)
distanceSensor = UltrasonicSensor(Port.C)
camera = PUPRemoteHub(Port.E)

colorSensor.lights.on(0)
distanceSensor.lights.on(100)
camera.add_command('blob', 'hhhhhh')

def linearMap(lmInput, lmInputMin, lmInputMax, lmOutputMin, lmOutputMax):
    return ((((lmOutputMax - lmOutputMin) * (lmInput - lmInputMin)) / (lmInputMax - lmInputMin)) + lmOutputMin)

def pid(pidError, pidKp, pidKi, pidKd, pidKm, pidErrorSummation, pidErrorPrevious):
    pidProportion = pidError * pidKp
    pidErrorSummation += pidError
    pidIntegral = pidErrorSummation * pidKi
    pidDerivative = (pidError - pidErrorPrevious) * pidKd
    pidErrorPrevious = pidError

    return pidErrorSummation, pidErrorPrevious, (pidKm * (pidProportion + pidIntegral + pidDerivative))

def pidPos(pidpLimit, pidpError, pidpKp, pidpKi, pidpKd, pidpKm, pidpErrorSummation, pidpErrorPrevious):
    pidpProportion = pidpError * pidpKp
    # pidpErrorSummation += pidpError
    pidpErrorSummation += 10 if (pidpError > 10) else pidpError
    pidpIntegral = pidpErrorSummation * pidpKi
    pidpDerivative = (pidpError - pidpErrorPrevious) * pidpKd
    pidpErrorPrevious = pidpError
    pidpValue = pidpKm * (pidpProportion + pidpIntegral + pidpDerivative)

    return pidpErrorSummation, pidpErrorPrevious, pidpValue if (pidpValue <= pidpLimit) else pidpLimit

def pidNeg(pidnLimit, pidnError, pidnKp, pidnKi, pidnKd, pidnKm, pidnErrorSummation, pidnErrorPrevious):
    pidnProportion = pidnError * pidnKp
    # pidnErrorSummation += pidnError
    pidnErrorSummation += -10 if (pidnError < -10) else pidnError
    pidnIntegral = pidnErrorSummation * pidnKi
    pidnDerivative = (pidnError - pidnErrorPrevious) * pidnKd
    pidnErrorPrevious = pidnError
    pidnValue = pidnKm * (pidnProportion + pidnIntegral + pidnDerivative)

    return pidnErrorSummation, pidnErrorPrevious, pidnValue if (pidnValue >= pidnLimit) else pidnLimit

def intHSV(ihsvReturnValue = -1):
    if (ihsvReturnValue == 0):
        return int(str(colorSensor.hsv()).split(",")[0].split("=")[1])
    elif (ihsvReturnValue == 1):
        return int(str(colorSensor.hsv()).split(",")[1].split("=")[1])
    elif (ihsvReturnValue == 2):
        return int(str(colorSensor.hsv()).split(",")[2].split("=")[1].split(")")[0])
    elif (ihsvReturnValue == -1):
        return [int(str(colorSensor.hsv()).split(",")[0].split("=")[1]), int(str(colorSensor.hsv()).split(",")[1].split("=")[1]), int(str(colorSensor.hsv()).split(",")[2].split("=")[1].split(")")[0])]

def getParking(gpDistanceTarget, gpDuration):
    if (gpDuration == 0):
        if (distanceSensor.distance() < gpDistanceTarget):
            return "Parking"
        else:
            return "Normal"

    else:
        gpDistanceMin = 2000
        gpClock = StopWatch()

        while (gpClock.time() < gpDuration):
            gpDistance = distanceSensor.distance()

            if (gpDistance < gpDistanceMin):
                gpDistanceMin = gpDistance

        if (gpDistanceMin < gpDistanceTarget):
            return "Parking"
        else:
            return "Normal"

def getTrafficSign():
    gtsCall = camera.call('blob')

    try:
        gtsGpix = gtsCall[2]
        gtsRpix = gtsCall[5]

        if (gtsGpix > gtsRpix):
            return ["Green", gtsGpix]
        elif (gtsRpix > gtsGpix):
            return ["Red", gtsRpix]
        else:
            return ["None", 0]

    except:
        return ["Error", -1]

def RECORDPARKING(rpDistance, rpDuration, rpInput, rpListValue, rpPosition, *, fixed = ""):
    if (rpInput == None):
        rpParking = (getParking(rpDistance, rpDuration) if (fixed == "") else fixed)
        rpListValue.append(rpParking)
        print(f"{rpPosition}{rpParking}", end = " ")

        return rpParking

    else:
        return rpInput

def RECORDTRAFFICSIGN(rtsInput, rtsListValue, rtsPosition, *, fixed = ""):
    if (rtsInput == None):
        rtsTrafficSign = (getTrafficSign() if (fixed == "") else fixed)
        rtsListValue.append(rtsTrafficSign)
        print(f"{rtsTrafficSign[1]} {rtsPosition}{rtsTrafficSign[0]}", end = (" " if (rtsPosition != "f") else "\n\n"))

        return rtsTrafficSign

    else:
        return rtsInput

class FutureEngineers:
    def __init__(self, driveMotor, steerMotor, visionMotor):
        self.driveMotor = driveMotor
        self.steerMotor = steerMotor
        self.visionMotor = visionMotor

        self.forwardStreetErrorKp = const(3)
        self.forwardStreetErrorKd = const(1.5)
        self.backwardStreetErrorKp = const(3)
        self.backwardStreetErrorKd = const(1.2)
        self.streetErrorKi = const(0.0000)

        self.forwardTurnErrorKp = const(2)
        self.forwardTurnErrorKi = const(0.0001)
        self.forwardTurnErrorKd = const(0.3)
        self.backwardTurnErrorKp = const(1)
        self.backwardTurnErrorKi = const(0.0001)
        self.backwardTurnErrorKd = const(0.3)

        self.forwardStallTorque = const(250)
        self.backwardStallTorque = const(300)
        self.forwardStallSpeed = const(150)
        self.backwardStallSpeed = const(0.7)

        self.forwardRightIncrement = const(-7)
        self.forwardLeftIncrement = const(10)
        self.backwardRightIncrement = const(-25)
        self.backwardLeftIncrement = const(15)

        self.accelMin = const(2000)

        self.driveMotor.control.limits(2000, self.accelMin, 1000)
        self.steerMotor.control.limits(2000, 20000, 1000)
        self.visionMotor.control.limits(2000, 20000, 1000)

        self.steerMotor.control.pid(ki = 93464, integral_deadzone = 8, integral_rate = 2000)

    def start(self):
        if (self.visionMotor.angle() > 180):
            self.visionMotor.reset_angle(self.visionMotor.angle() - 360)
        elif (self.visionMotor.angle() < -180):
            self.visionMotor.reset_angle(self.visionMotor.angle() + 360)
    
    def look(self, lookAngle, lookBool):
        self.visionMotor.run_target(1000, lookAngle, Stop.HOLD, lookBool)

    def fastAcceleration(self, fastAccelerationBool):
        self.driveMotor.control.limits(acceleration = (20000 if fastAccelerationBool else self.accelMin))

    def move(self, moveSpeed, moveSteer):
        self.driveMotor.run(moveSpeed)
        self.steerMotor.run_target(1000, moveSteer, Stop.HOLD, False)

    def HOLD(self, holdDuration = 0):
        self.driveMotor.control.limits(speed = 10, torque = 1)
        self.driveMotor.hold()

        holdClock = StopWatch()
        holdClock.reset()
        hub.speaker.beep(500, 10)

        while (holdClock.time() < holdDuration):
            pass

        hub.speaker.beep(500, 10)
        self.driveMotor.control.limits(speed = 2000, torque = 1000)

    def permanentHold(self, permanentHoldPrint = 0):
        self.HOLD(300)
        print(f"Time: {clock.time()}")

        for _ in range(permanentHoldPrint):
            print(f"End: {hub.imu.heading()}")
            wait(800)
            
        print("\n\n\n")
        self.steerMotor.run_target(1000, 0, Stop.HOLD, False)
        wait(700)
        end

    def FINISHINGHOLD(self, finishingHoldSteer = None):
        self.driveMotor.control.limits(speed = 10, torque = 1)
        self.driveMotor.hold()

        if (finishingHoldSteer == None):
            finishingHoldSteer = self.steerMotor.angle()

        while (abs(self.driveMotor.speed()) > 50):
            pass

        for i in range(5):
            self.steerMotor.run_target(1000, finishingHoldSteer, Stop.HOLD, False)
            wait(750)     
            hub.speaker.beep(500, 250)

        wait(300)

        self.driveMotor.control.limits(speed = 2000, torque = 1000)       

    def motorClose(self):
        self.driveMotor.close()
        self.steerMotor.close()
        self.visionMotor.close()

    def CAMERASCAN(self, cameraScanAngleInitial, cameraScanAngleFinal, cameraScanSpeed, cameraScanInput, cameraScanListValue, cameraScanPosition):
        if (cameraScanInput == None):
            cameraScanReturn, cameraScanRecord, cameraScanGreenCtr, cameraScanRedCtr, cameraScanGreenMax, cameraScanRedMax = "", [], 0, 0, 0, 0

            self.look(cameraScanAngleInitial, True)

            if (cameraScanAngleFinal > cameraScanAngleInitial):
                while (self.visionMotor.angle() < (cameraScanAngleFinal - 2)):
                    self.visionMotor.run_target(cameraScanSpeed, cameraScanAngleFinal, Stop.HOLD, False)
                    cameraScanRecord.append(getTrafficSign())
                    hub.speaker.beep(500, 10)

            else:
                while (self.visionMotor.angle() > (cameraScanAngleFinal + 2)):
                    self.visionMotor.run_target(cameraScanSpeed, cameraScanAngleFinal, Stop.HOLD, False)
                    cameraScanRecord.append(getTrafficSign())
                    hub.speaker.beep(500, 10)

            for _ in range(cameraScanRecord.count(["None", 0])):
                cameraScanRecord.remove(["None", 0])
            
            for i in range(len(cameraScanRecord)):
                x, y = cameraScanRecord[i]

                if (x == "Green"):
                    cameraScanGreenCtr += 1
                    if (y > cameraScanGreenMax):
                        cameraScanGreenMax = y

                elif (x == "Red"):
                    cameraScanRedCtr += 1
                    if (y > cameraScanRedMax):
                        cameraScanRedMax = y

            if (cameraScanGreenCtr > cameraScanRedCtr):
                cameraScanReturn = ["Green", cameraScanGreenMax]
            elif (cameraScanRedCtr > cameraScanGreenCtr):
                cameraScanReturn = ["Red", cameraScanRedMax]
            else:
                cameraScanReturn = ["None", 0]

            return RECORDTRAFFICSIGN(cameraScanInput, cameraScanListValue, cameraScanPosition, fixed = cameraScanReturn)

        else:
            return cameraScanInput

    def street(self, streetDuration, streetHeadingTarget, streetSpeedInitial, streetSpeedFinal):
        streetSpeed, streetErrorKm, streetErrorSummation, streetErrorPrevious, streetErrorCorrection = 0, 1, 0, 0, 0

        streetMotorAngleStart = self.driveMotor.angle()
        streetMotorAngleTarget = streetMotorAngleStart + streetDuration

        streetHeadingStart = hub.imu.heading()

        if (abs(streetHeadingTarget - streetHeadingStart) <= 13):
            if (streetDuration > 0):
                while (self.driveMotor.angle() < streetMotorAngleTarget):
                    streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                    streetErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                    streetErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                    streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pid((streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)
                    
                    self.move(streetSpeed, streetErrorCorrection)
                    
            else:
                streetSpeedInitial *= -1
                streetSpeedFinal *= -1
                streetErrorKm *= -1

                while (self.driveMotor.angle() > streetMotorAngleTarget):
                    streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                    streetErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                    streetErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                    streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pid((streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)
                    
                    self.move(streetSpeed, streetErrorCorrection)

        else:
            if (streetDuration > 0):
                if (streetHeadingTarget > streetHeadingStart):
                    while (self.driveMotor.angle() < streetMotorAngleTarget):
                        streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                        streetErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                        streetErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidPos(40, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)

                        self.move(streetSpeed, streetErrorCorrection)

                else:
                    while (self.driveMotor.angle() < streetMotorAngleTarget):
                        streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                        streetErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                        streetErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidNeg(-40, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)

                        self.move(streetSpeed, streetErrorCorrection)

            else:
                streetSpeedInitial *= -1
                streetSpeedFinal *= -1
                streetErrorKm *= -1

                if (streetHeadingTarget > streetHeadingStart):
                    while (self.driveMotor.angle() > streetMotorAngleTarget):
                        streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                        streetErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                        streetErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidNeg(-40, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)
                        
                        self.move(streetSpeed, streetErrorCorrection)

                else:
                    while (self.driveMotor.angle() > streetMotorAngleTarget):
                        streetSpeed = linearMap(self.driveMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal)
                        streetErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                        streetErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidPos(40, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, self.streetErrorKi, streetErrorKd, streetErrorKm, streetErrorSummation, streetErrorPrevious)
                        
                        self.move(streetSpeed, streetErrorCorrection)

    def streetStall(self, streetStallDurationInitial, streetStallHeadingTarget, streetStallSpeedInitial, streetStallSpeedFinal, streetStallDurationFinal):
        streetStallErrorKm, streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = 1, 0, 0, 0

        self.street(streetStallDurationInitial, streetStallHeadingTarget, streetStallSpeedInitial, streetStallSpeedFinal)
        hub.speaker.beep(500, 10)

        if (streetStallDurationInitial > 0):
            self.driveMotor.control.limits(torque = self.forwardStallTorque)

            while (self.driveMotor.speed() > self.forwardStallSpeed):
                streetStallErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                streetStallErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, self.streetErrorKi, streetStallErrorKd, streetStallErrorKm, streetStallErrorSummation, streetStallErrorPrevious)

                self.move(streetStallSpeedFinal, streetStallErrorCorrection)

        else:
            streetStallSpeedFinal *= -1
            streetStallErrorKm *= -1

            self.driveMotor.control.limits(torque = self.backwardStallTorque)

            while (self.driveMotor.speed() < streetStallSpeedFinal * self.backwardStallSpeed):
                streetStallErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                streetStallErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, self.streetErrorKi, streetStallErrorKd, streetStallErrorKm, streetStallErrorSummation, streetStallErrorPrevious)

                self.move(streetStallSpeedFinal, streetStallErrorCorrection)

        self.driveMotor.control.limits(torque = 1000)
        self.driveMotor.run(streetStallSpeedFinal)
        self.fastAcceleration(False)
        hub.speaker.beep(500, streetStallDurationFinal)
        self.driveMotor.hold()
        self.driveMotor.reset_angle(0)
        hub.imu.reset_heading(0)

    def streetLine(self, streetLineDuration, streetLineHeadingTarget, streetLineSpeedInitial, streetLineSpeedFinal):
        streetLineErrorKm, streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = 1, 0, 0, 0

        self.street(streetLineDuration, streetLineHeadingTarget, streetLineSpeedInitial, streetLineSpeedFinal)
        hub.speaker.beep(500, 10)

        streetLineSpeedMax, streetLineErrorKpMax, streetLineErrorKdMax = 1000, 0, 0

        if (streetLineDuration > 0):
            streetLineErrorKpMax = self.forwardStreetErrorKp
            streetLineErrorKdMax = self.forwardStreetErrorKd

        else:
            streetLineSpeedFinal *= -1
            streetLineSpeedMax *= -1
            streetLineErrorKm *= -1
            streetLineErrorKpMax = self.backwardStreetErrorKp
            streetLineErrorKdMax = self.backwardStreetErrorKd

        while (intHSV(1) < 30):
            streetLineErrorKp = linearMap(self.driveMotor.speed(), 0, streetLineSpeedMax, 0, streetLineErrorKpMax)
            streetLineErrorKd = linearMap(self.driveMotor.speed(), 0, streetLineSpeedMax, 0, streetLineErrorKdMax)
            streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = pid((streetLineHeadingTarget - hub.imu.heading()), streetLineErrorKp, self.streetErrorKi, streetLineErrorKd, streetLineErrorKm, streetLineErrorSummation, streetLineErrorPrevious)

            self.move(streetLineSpeedFinal, streetLineErrorCorrection)

    def streetDetermineIfLine(self, streetIfLineDuration, streetIfLineHeadingTarget, streetIfLineSpeedInitial, streetIfLineSpeedFinal):
        streetIfLineSpeed, streetIfLineErrorKm, streetIfLineErrorSummation, streetIfLineErrorPrevious, streetIfLineErrorCorrection = 0, 1, 0, 0, 0

        streetIfLineMotorAngleStart = self.driveMotor.angle()
        streetIfLineMotorAngleTarget = streetIfLineMotorAngleStart + streetIfLineDuration

        streetIfLineSatMax, streetIfLineSat = 0, 0

        if (streetIfLineDuration > 0):
            while (self.driveMotor.angle() < streetIfLineMotorAngleTarget):
                streetIfLineSpeed = linearMap(self.driveMotor.angle(), streetIfLineMotorAngleStart, streetIfLineMotorAngleTarget, streetIfLineSpeedInitial, streetIfLineSpeedFinal)
                streetIfLineErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                streetIfLineErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                streetIfLineErrorSummation, streetIfLineErrorPrevious, streetIfLineErrorCorrection = pid((streetIfLineHeadingTarget - hub.imu.heading()), streetIfLineErrorKp, self.streetErrorKi, streetIfLineErrorKd, streetIfLineErrorKm, streetIfLineErrorSummation, streetIfLineErrorPrevious)

                self.move(streetIfLineSpeed, streetIfLineErrorCorrection)

                streetIfLineSat = intHSV(1)

                if (streetIfLineSat > streetIfLineSatMax):
                    streetIfLineSatMax = streetIfLineSat

        else:
            streetIfLineSpeedInitial *= -1
            streetIfLineSpeedFinal *= -1
            streetIfLineErrorKm *= -1
            
            while (self.driveMotor.angle() > streetIfLineMotorAngleTarget):
                streetIfLineSpeed = linearMap(self.driveMotor.angle(), streetIfLineMotorAngleStart, streetIfLineMotorAngleTarget, streetIfLineSpeedInitial, streetIfLineSpeedFinal)
                streetIfLineErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                streetIfLineErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                streetIfLineErrorSummation, streetIfLineErrorPrevious, streetIfLineErrorCorrection = pid((streetIfLineHeadingTarget - hub.imu.heading()), streetIfLineErrorKp, self.streetErrorKi, streetIfLineErrorKd, streetIfLineErrorKm, streetIfLineErrorSummation, streetIfLineErrorPrevious)

                self.move(streetIfLineSpeed, streetIfLineErrorCorrection)

                streetIfLineSat = intHSV(1)

                if (streetIfLineSat > streetIfLineSatMax):
                    streetIfLineSatMax = streetIfLineSat

        if (streetIfLineSatMax > 35):
            return "Line"
        else: 
            return "No Line"

    def streetDetermineTheLine(self, streetTheLineDuration, streetTheLineHeadingTarget, streetTheLineSpeedInitial, streetTheLineSpeedFinal):
        self.streetLine(streetTheLineDuration, streetTheLineHeadingTarget, streetTheLineSpeedInitial, streetTheLineSpeedFinal)

        streetTheLineHueMax, streetTheLineHue = 0, 0

        while (intHSV(1) > 15):
            streetTheLineHue = intHSV(0)

            if (streetTheLineHue > streetTheLineHueMax):
                hub.speaker.beep(500, 10)
                streetTheLineHueMax = streetTheLineHue

        if (190 < streetTheLineHueMax and streetTheLineHueMax < 290):
            return -1
        else:
            return 1

    def STREETSCAN(self, streetScanDuration, streetScanHeadingTarget, streetScanSpeed, streetScanInput, streetScanListValue, streetScanPosition):
        streetScanErrorKm, streetScanErrorSummation, streetScanErrorPrevious, streetScanErrorCorrection = 1, 0, 0, 0

        streetScanMotorAngleStart = self.driveMotor.angle()
        streetScanMotorAngleTarget = streetScanMotorAngleStart + streetScanDuration

        streetScanReturn, streetScanRecord, streetScanGreenCtr, streetScanRedCtr, streetScanGreenMax, streetScanRedMax = "", [], 0, 0, 0, 0

        if (streetScanDuration > 0):
            while (self.driveMotor.angle() < streetScanMotorAngleTarget):
                streetScanErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                streetScanErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                streetScanErrorSummation, streetScanErrorPrevious, streetScanErrorCorrection = pid((streetScanHeadingTarget - hub.imu.heading()), streetScanErrorKp, self.streetErrorKi, streetScanErrorKd, streetScanErrorKm, streetScanErrorSummation, streetScanErrorPrevious)

                self.move(streetScanSpeed, streetScanErrorCorrection)

                streetScanRecord.append(getTrafficSign())
                hub.speaker.beep(500, 10)

        else:
            streetScanSpeed *= -1
            streetScanErrorKm *= -1

            while (self.driveMotor.angle() > streetScanMotorAngleTarget):
                streetScanErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                streetScanErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                streetScanErrorSummation, streetScanErrorPrevious, streetScanErrorCorrection = pid((streetScanHeadingTarget - hub.imu.heading()), streetScanErrorKp, self.streetErrorKi, streetScanErrorKd, streetScanErrorKm, streetScanErrorSummation, streetScanErrorPrevious)

                self.move(streetScanSpeed, streetScanErrorCorrection)

                streetScanRecord.append(getTrafficSign())
                hub.speaker.beep(500, 10)
        
        for _ in range(streetScanRecord.count(["None", 0])):
            streetScanRecord.remove(["None", 0])
        
        for i in range(len(streetScanRecord)):
            x, y = streetScanRecord[i]

            if (x == "Green"):
                streetScanGreenCtr += 1
                if (y > streetScanGreenMax):
                    streetScanGreenMax = y

            elif (x == "Red"):
                streetScanRedCtr += 1
                if (y > streetScanRedMax):
                    streetScanRedMax = y

        if (streetScanGreenCtr > streetScanRedCtr):
            streetScanReturn = ["Green", streetScanGreenMax]
        elif (streetScanRedCtr > streetScanGreenCtr):
            streetScanReturn = ["Red", streetScanRedMax]
        else:
            streetScanReturn = ["None", 0]

        return RECORDTRAFFICSIGN(streetScanInput, streetScanListValue, streetScanPosition, fixed = streetScanReturn)

    def STREETREAD(self, streetReadDuration, streetReadHeadingTarget, streetReadSpeed, streetReadDistanceTarget, streetReadInput, streetReadListValue, streetReadPosition):
        self.street(-20, streetReadHeadingTarget, streetReadSpeed, streetReadSpeed)

        streetReadErrorKm, streetReadErrorSummation, streetReadErrorPrevious, streetReadErrorCorrection = 1, 0, 0, 0

        streetReadMotorAngleStart = self.driveMotor.angle()
        streetReadMotorAngleTarget = streetReadMotorAngleStart + streetReadDuration

        streetReadReturn, streetReadDistanceMin, streetReadDistance = "", 2000, 0

        if (streetReadDuration > 0):
            streetReadDuration -= 20

            while (self.driveMotor.angle() < streetReadMotorAngleTarget):
                streetReadErrorKp = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKp)
                streetReadErrorKd = linearMap(self.driveMotor.speed(), 0, 1000, 0, self.forwardStreetErrorKd)
                streetReadErrorSummation, streetReadErrorPrevious, streetReadErrorCorrection = pid((streetReadHeadingTarget - hub.imu.heading()), streetReadErrorKp, self.streetErrorKi, streetReadErrorKd, streetReadErrorKm, streetReadErrorSummation, streetReadErrorPrevious)

                self.move(streetReadSpeed, streetReadErrorCorrection)

                streetReadDistance = distanceSensor.distance()

                if (streetReadDistance < streetReadDistanceMin):
                    streetReadDistanceMin = streetReadDistance

        else:
            streetReadSpeed *= -1
            streetReadErrorKm *= -1

            streetReadDuration += 20

            while (self.driveMotor.angle() > streetReadMotorAngleTarget):
                streetReadErrorKp = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKp)
                streetReadErrorKd = linearMap(self.driveMotor.speed(), 0, -1000, 0, self.backwardStreetErrorKd)
                streetReadErrorSummation, streetReadErrorPrevious, streetReadErrorCorrection = pid((streetReadHeadingTarget - hub.imu.heading()), streetReadErrorKp, self.streetErrorKi, streetReadErrorKd, streetReadErrorKm, streetReadErrorSummation, streetReadErrorPrevious)

                self.move(streetReadSpeed, streetReadErrorCorrection)

                streetReadDistance = distanceSensor.distance()

                if (streetReadDistance < streetReadDistanceMin):
                    streetReadDistanceMin = streetReadDistance

        if (streetReadDistanceMin < streetReadDistanceTarget):
            streetReadReturn = "Parking"
        else:
            streetReadReturn = "Normal"

        return RECORDPARKING(0, 0, streetReadInput, streetReadListValue, streetReadPosition, fixed = streetReadReturn)

    def drive(self, driveDuration, driveSpeedInitial, driveSpeedFinal, driveSteerInitial, driveSteerFinal):
        driveSpeed, driveSteer = 0, 0

        driveMotorAngleStart = self.driveMotor.angle()
        driveMotorAngleTarget = driveMotorAngleStart + driveDuration

        if (driveDuration > 0):
            while (self.driveMotor.angle() < driveMotorAngleTarget):
                driveSpeed = linearMap(self.driveMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal)
                driveSteer = linearMap(self.driveMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSteerInitial, driveSteerFinal)

                self.move(driveSpeed, driveSteer)

        else:
            driveSpeedInitial *= -1
            driveSpeedFinal *= -1

            while (self.driveMotor.angle() > driveMotorAngleTarget):
                driveSpeed = linearMap(self.driveMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal)
                driveSteer = linearMap(self.driveMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSteerInitial, driveSteerFinal)

                self.move(driveSpeed, driveSteer)

    def driveLine(self, driveLineDuration, driveLineSpeedInitial, driveLineSpeedFinal, driveLineSteerInitial, driveLineSteerFinal):
        self.drive(driveLineDuration, driveLineSpeedInitial, driveLineSpeedFinal, driveLineSteerInitial, driveLineSteerFinal)

        self.move(driveLineSpeedFinal * abs(driveLineDuration) / driveLineDuration, driveLineSteerFinal * abs(driveLineDuration) / driveLineDuration)
        hub.speaker.beep(500, 10)

        while (intHSV(1) < 35): 
            pass

    def turnSemi(self, turnSemiDirection, turnSemiHeadingTarget, turnSemiHeadingBasis, turnSemiSteerLimit, turnSemiSpeedInitial, turnSemiSpeedFinal):
        turnSemiError, turnSemiSpeed, turnSemiErrorKm, turnSemiErrorSummation, turnSemiErrorPrevious, turnSemiErrorCorrection = 0, 0, 1, 0, 0, 0
        
        turnSemiHeadingStart = hub.imu.heading()
        turnSemiHeadingDifference = turnSemiHeadingTarget - turnSemiHeadingStart

        if (turnSemiDirection > 0):
            if (turnSemiHeadingTarget > turnSemiHeadingStart):
                turnSemiHeadingTarget += self.forwardRightIncrement
                turnSemiHeadingBasis += self.forwardRightIncrement

                while (hub.imu.heading() < turnSemiHeadingTarget):
                    turnSemiError = turnSemiHeadingBasis - hub.imu.heading()
                    turnSemiSpeed = linearMap(turnSemiError, turnSemiHeadingDifference, 0, turnSemiSpeedInitial, turnSemiSpeedFinal)
                    turnSemiErrorSummation, turnSemiErrorPrevious, turnSemiErrorCorrection = pidPos(turnSemiSteerLimit, turnSemiError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnSemiErrorKm, turnSemiErrorSummation, turnSemiErrorPrevious)

                    self.move(turnSemiSpeed, turnSemiErrorCorrection)

            else:
                turnSemiSteerLimit *= -1
                turnSemiHeadingTarget += self.forwardLeftIncrement
                turnSemiHeadingBasis += self.forwardLeftIncrement
                
                while (hub.imu.heading() > turnSemiHeadingTarget):
                    turnSemiError = turnSemiHeadingBasis - hub.imu.heading()
                    turnSemiSpeed = linearMap(turnSemiError, turnSemiHeadingDifference, 0, turnSemiSpeedInitial, turnSemiSpeedFinal)
                    turnSemiErrorSummation, turnSemiErrorPrevious, turnSemiErrorCorrection = pidNeg(turnSemiSteerLimit, turnSemiError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnSemiErrorKm, turnSemiErrorSummation, turnSemiErrorPrevious)

                    self.move(turnSemiSpeed, turnSemiErrorCorrection)

        else:
            turnSemiSpeedInitial *= -1
            turnSemiSpeedFinal *= -1
            turnSemiErrorKm *= -1

            if (turnSemiHeadingTarget > turnSemiHeadingStart):
                turnSemiSteerLimit *= -1
                turnSemiHeadingTarget += self.backwardRightIncrement
                turnSemiHeadingBasis += self.backwardRightIncrement

                while (hub.imu.heading() < turnSemiHeadingTarget):
                    turnSemiError = turnSemiHeadingBasis - hub.imu.heading()
                    turnSemiSpeed = linearMap(turnSemiError, turnSemiHeadingDifference, 0, turnSemiSpeedInitial, turnSemiSpeedFinal)
                    turnSemiErrorSummation, turnSemiErrorPrevious, turnSemiErrorCorrection = pidNeg(turnSemiSteerLimit, turnSemiError, self.backwardTurnErrorKp, self.backwardTurnErrorKi, self.backwardTurnErrorKd, turnSemiErrorKm, turnSemiErrorSummation, turnSemiErrorPrevious)

                    self.move(turnSemiSpeed, turnSemiErrorCorrection)

            else:
                turnSemiHeadingTarget += self.backwardLeftIncrement
                turnSemiHeadingBasis += self.backwardLeftIncrement

                while (hub.imu.heading() > turnSemiHeadingTarget):
                    turnSemiError = turnSemiHeadingBasis - hub.imu.heading()
                    turnSemiSpeed = linearMap(turnSemiError, turnSemiHeadingDifference, 0, turnSemiSpeedInitial, turnSemiSpeedFinal)
                    turnSemiErrorSummation, turnSemiErrorPrevious, turnSemiErrorCorrection = pidPos(turnSemiSteerLimit, turnSemiError, self.backwardTurnErrorKp, self.backwardTurnErrorKi, self.backwardTurnErrorKd, turnSemiErrorKm, turnSemiErrorSummation, turnSemiErrorPrevious)

                    self.move(turnSemiSpeed, turnSemiErrorCorrection)

        hub.speaker.beep(500, 10)

    def turnStall(self, turnStallDirection, turnStallHeadingInitial, turnStallHeadingBasis, turnStallSteerLimit, turnStallSpeedInitial, turnStallSpeedFinal, turnStallDurationFinal):
        self.turnSemi(turnStallDirection, turnStallHeadingInitial, turnStallHeadingBasis, turnStallSteerLimit, turnStallSpeedInitial, turnStallSpeedFinal)

        turnStallError, turnStallSpeed, turnStallErrorKm, turnStallErrorSummation, turnStallErrorPrevious, turnStallErrorCorrection = 0, 0, 1, 0, 0, 0

        turnStallHeadingStart = turnStallHeadingInitial
        turnStallHeadingDifference = turnStallHeadingBasis - turnStallHeadingStart

        if (turnStallDirection > 0):
            self.driveMotor.control.limits(torque = self.forwardStallTorque)

            if (turnStallHeadingBasis >= turnStallHeadingInitial):
                while (self.driveMotor.speed() > self.forwardStallSpeed):
                    turnStallError = turnStallHeadingBasis - hub.imu.heading()
                    turnStallSpeed = linearMap(turnStallError, turnStallHeadingDifference, 0, turnStallSpeedInitial, turnStallSpeedFinal)
                    turnStallErrorSummation, turnStallErrorPrevious, turnStallErrorCorrection = pidPos(turnStallSteerLimit, turnStallError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnStallErrorKm, turnStallErrorSummation, turnStallErrorPrevious)

                    self.move(turnStallSpeed, turnStallErrorCorrection)

            else:
                turnStallSteerLimit *= -1

                while (self.driveMotor.speed() > self.forwardStallSpeed):
                    turnStallError = turnStallHeadingBasis - hub.imu.heading()
                    turnStallSpeed = linearMap(turnStallError, turnStallHeadingDifference, 0, turnStallSpeedInitial, turnStallSpeedFinal)
                    turnStallErrorSummation, turnStallErrorPrevious, turnStallErrorCorrection = pidNeg(turnStallSteerLimit, turnStallError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnStallErrorKm, turnStallErrorSummation, turnStallErrorPrevious)

                    self.move(turnStallSpeed, turnStallErrorCorrection)

        else:
            self.driveMotor.control.limits(torque = self.backwardStallTorque)

            turnStallSpeedInitial *= -1
            turnStallSpeedFinal *= -1
            turnStallErrorKm *= -1

            if (turnStallHeadingBasis >= turnStallHeadingInitial):
                turnStallSteerLimit *= -1

                while (self.driveMotor.speed() < turnStallSpeedFinal * self.backwardStallSpeed * 0.8):
                    turnStallError = turnStallHeadingBasis - hub.imu.heading()
                    turnStallSpeed = linearMap(turnStallError, turnStallHeadingDifference, 0, turnStallSpeedInitial, turnStallSpeedFinal)
                    turnStallErrorSummation, turnStallErrorPrevious, turnStallErrorCorrection = pidNeg(turnStallSteerLimit, turnStallError, self.backwardTurnErrorKp, self.backwardTurnErrorKi, self.backwardTurnErrorKd, turnStallErrorKm, turnStallErrorSummation, turnStallErrorPrevious)

                    self.move(turnStallSpeed, turnStallErrorCorrection)

            else:
                while (self.driveMotor.speed() < turnStallSpeedFinal * self.backwardStallSpeed * 0.8):
                    turnStallError = turnStallHeadingBasis - hub.imu.heading()
                    turnStallSpeed = linearMap(turnStallError, turnStallHeadingDifference, 0, turnStallSpeedInitial, turnStallSpeedFinal)
                    turnStallErrorSummation, turnStallErrorPrevious, turnStallErrorCorrection = pidPos(turnStallSteerLimit, turnStallError, self.backwardTurnErrorKp, self.backwardTurnErrorKi, self.backwardTurnErrorKd, turnStallErrorKm, turnStallErrorSummation, turnStallErrorPrevious)

                    self.move(turnStallSpeed, turnStallErrorCorrection)

        self.driveMotor.control.limits(torque = 1000)
        self.driveMotor.run(turnStallSpeedFinal)
        hub.speaker.beep(500, turnStallDurationFinal)
        self.driveMotor.hold()
        self.driveMotor.reset_angle(0)
        hub.imu.reset_heading(0)

    def turnDetermineIfLine(self, turnIfLineDirection, turnIfLineHeadingTarget, turnIfLineSteerLimit, turnIfLineSpeedInitial, turnIfLineSpeedFinal):
        turnIfLineError, turnIfLineSpeed, turnIfLineErrorKm, turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = 0, 0, 1, 0, 0, 0

        turnIfLineHeadingStart = hub.imu.heading()
        turnIfLineHeadingDifference = turnIfLineHeadingTarget - turnIfLineHeadingStart

        turnIfLineSatMax, turnIfLineSat = 0, 0

        if (turnIfLineDirection > 0):
            if (turnIfLineHeadingTarget > turnIfLineHeadingStart):
                turnIfLineHeadingTarget += self.forwardRightIncrement

                while (hub.imu.heading() < turnIfLineHeadingTarget):
                    turnIfLineError = turnIfLineHeadingTarget - hub.imu.heading()
                    turnIfLineSpeed = linearMap(turnIfLineError, turnIfLineHeadingDifference, 0, turnIfLineSpeedInitial, turnIfLineSpeedFinal)
                    turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = pidPos(turnIfLineSteerLimit, turnIfLineError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnIfLineErrorKm, turnIfLineErrorSummation, turnIfLineErrorPrevious)

                    self.move(turnIfLineSpeed, turnIfLineErrorCorrection)

                    turnIfLineSat = intHSV(1)

                    if (turnIfLineSat > turnIfLineSatMax):
                        turnIfLineSatMax = turnIfLineSat

            else:
                turnIfLineSteerLimit *= -1
                turnIfLineHeadingTarget += self.forwardLeftIncrement

                while (hub.imu.heading() > turnIfLineHeadingTarget):
                    turnIfLineError = turnIfLineHeadingTarget - hub.imu.heading()
                    turnIfLineSpeed = linearMap(turnIfLineError, turnIfLineHeadingDifference, 0, turnIfLineSpeedInitial, turnIfLineSpeedFinal)
                    turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = pidNeg(turnIfLineSteerLimit, turnIfLineError, self.forwardTurnErrorKp, self.forwardTurnErrorKi, self.forwardTurnErrorKd, turnIfLineErrorKm, turnIfLineErrorSummation, turnIfLineErrorPrevious)

                    self.move(turnIfLineSpeed, turnIfLineErrorCorrection)

                    turnIfLineSat = intHSV(1)

                    if (turnIfLineSat > turnIfLineSatMax):
                        turnIfLineSatMax = turnIfLineSat

        else: 
            turnIfLineSpeedInitial *= -1
            turnIfLineSpeedFinal *= -1
            turnIfLineErrorKm *= -1

            # di pa tapos

        if (turnIfLineSatMax > 35): 
            return "Line"
        else:
            return "No Line"

    def turn(self, turnDirection, turnHeadingTarget, turnSteerLimit, turnSpeedInitial, turnSpeedFinal):
        self.turnSemi(turnDirection, turnHeadingTarget, turnHeadingTarget, turnSteerLimit, turnSpeedInitial, turnSpeedFinal)

def main():
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    monke.fastAcceleration(False)
    monke.street(150, 0, 2000, 2000)
    monke.fastAcceleration(True)
    monke.street(1000, 0, 2000, 2000)
    monke.finishHold(12, 12)
    monke.street(-100, 0, 2000, 2000)

if __name__ == "__main__":
    print("\n\n\n")
    main()
