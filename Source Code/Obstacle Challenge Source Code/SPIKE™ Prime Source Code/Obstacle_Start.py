from FE_Functions import *

def obstacleStart():
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)
    monke.start()

    linePresence, parking, trafficSign = "", "", ""

    print(f"\n\n\nVoltage: {hub.battery.voltage()}")
    hub.imu.reset_heading(0)
    monke.driveMotor.reset_angle(0)
    monke.HOLD()
    wait(500)

    clock.reset()
    
    steerMotor.run_target(1000, 0, Stop.HOLD, False)

    while (clock.time() < 400):
        monke.look(-90, False)

    while (clock.time() < 800):
        monke.look(90, False)

    while (clock.time() < 1200):
        monke.look(0, False)

    hub.speaker.beep(500, 100)

    _robotDirection = 0
    _distanceMin = 2000

    clock.reset()

    while (clock.time() < 500):
        if (distanceSensor.distance() < _distanceMin):
            _distanceMin = distanceSensor.distance()

    print(f"Front: {_distanceMin}", end = " ")

    if (970 < _distanceMin and _distanceMin < 1200):
        print("Laps: 0\t\t\b\b\b\b\bfStart")

        _robotDirection = monke.streetDetermineTheLine(10, 0, 2000, 2000)

        monke.look(90 * _robotDirection, False)

        if (_robotDirection == 1):
            # CLOCKWISE

            monke.turn(1, -30, 40, 2000, 2000)
            monke.street(200, -30, 2000, 2000)
            monke.streetStall(200, 0, 2000, 2000, 100)

        else:
            # COUNTERCLOCKWISE

            monke.streetStall(650, 0, 2000, 2000, 100)

    else:
        cameraCall = camera.call('blob')

        trafficSign = []

        try:
            gPix = cameraCall[2]
            rPix = cameraCall[5]

            if (gPix > rPix):
                trafficSign = ["Green", cameraCall[0]]
            elif (rPix > gPix):
                trafficSign = ["Red", cameraCall[3]]
            else:
                trafficSign = ["None", 0]

        except:
            trafficSign = ["Error", -1]

        print(f"{trafficSign[0]} x={trafficSign[1]}", end = " ")

        if (trafficSign[0] == "Green"):
            # GREEN

            if (trafficSign[1] < 150):
                # GREEN LEFT

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(400, -63, 800, 800)

                linePresence = monke.turnDetermineIfLine(1, 0, 40, 800, 800)

                if (linePresence == "Line"):
                    _robotDirection = -1
                    monke.street(300, 0, 2000, 2000)
                else:
                    linePresence = monke.streetDetermineIfLine(300, 0, 2000, 2000)

                    if (linePresence == "Line"):
                        _robotDirection = -1
                    else:
                        _robotDirection = 1

                if (_robotDirection == 1):
                    # GREEN LEFT CLOCKWISE

                    monke.turn(1, 42, 40, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.streetStall(400, 0, 2000, 850, 100)

                else:
                    # GREEN LEFT COUNTERCLOCKWISE

                    monke.turn(1, 45, 40, 2000, 2000)
                    monke.street(156, 45, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.streetStall(300, 0, 2000, 2000, 100)

            else:
                # GREEN RIGHT

                monke.fastAcceleration(False)
                monke.street(150, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(430, -20, 800, 2000)
                monke.turn(1, 0, 40, 2000, 2000)

                _robotDirection = monke.streetDetermineTheLine(200, 0, 2000, 2000)

                if (_robotDirection == 1):
                    # GREEN RIGHT CLOCKWISE

                    monke.look(RIGHT, False)
                    monke.streetStall(550, 0, 1000, 900, 100)

                else:
                    # GREEN RIGHT COUNTERCLOCKWISE

                    monke.turn(1, 32, 40, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.turn(1, 0, 40, 2000, 2000)
                    monke.streetStall(120, 0, 1000, 900, 100)

        else:
            # RED

            if (trafficSign[1] > 150):
                # RED RIGHT

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(400, 60, 800, 800)

                linePresence = monke.turnDetermineIfLine(1, 0, 40, 800, 800)

                if (linePresence == "Line"):
                    _robotDirection = 1
                    monke.street(300, 0, 2000, 2000)
                else:
                    linePresence = monke.streetDetermineIfLine(300, 0, 2000, 2000)

                    if (linePresence == "Line"):
                        _robotDirection = 1
                    else:
                        _robotDirection = -1

                if (_robotDirection == -1):
                    # RED RIGHT COUNTERCLOCKWISE

                    monke.turn(1, -50, 40, 2000, 2000)
                    monke.street(100, -50, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.streetStall(450, 0, 2000, 2000, 100)

                else:
                    # RED RIGHT CLOCKWISE

                    monke.turn(1, -55, 40, 2000, 2000)
                    monke.street(350, -55, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.streetStall(250, 0, 2000, 2000, 100)

            else:
                # RED LEFT

                monke.fastAcceleration(False)
                monke.street(150, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(400, 20, 800, 7000)
                monke.turn(1, 0, 40, 2000, 2000)
                _robotDirection = monke.streetDetermineTheLine(200, 0, 2000, 2000)

                if (_robotDirection == 1):
                    # RED LEFT CLOCKWISE

                    monke.turn(1, -50, 40, 2000, 2000)
                    monke.street(100, -50, 2000, 1000)
                    monke.look(RIGHT, False)
                    monke.turn(1, 0, 40, 1000, 800)
                    monke.streetStall(1, 0, 2000, 2000, 100)
                    
                else: 
                    # RED LEFT COUNTERCLOCKWISE

                    monke.turn(1, -40, 40, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.streetStall(200, 0, 2000, 2000, 100)

    monke.motorClose()

    if (_robotDirection == 1):
        print("CLOCKWISE\n")
    else:
        print("COUNTERCLOCKWISE\n")
        
    return _robotDirection

if __name__ == "__main__":
    print(f"\nVoltage: {hub.battery.voltage()}")
    hub.speaker.beep(500)

    try:
        obstacleStart()
    finally:
        print(f"\nTime: {clock.time()}")

        wait(1000)

        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        v.run_target(1000, 0, Stop.HOLD, False)
        s.run_target(1000, 0, Stop.HOLD, False)
        wait(800)
