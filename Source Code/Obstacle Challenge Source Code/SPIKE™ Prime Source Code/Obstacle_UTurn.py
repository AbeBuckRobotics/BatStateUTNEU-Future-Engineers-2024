from FE_Functions import *

def obstacleUTurn(robotDirection, recordListInput):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    if (visionMotor.angle() > 180):
        visionMotor.reset_angle(visionMotor.angle() - 360)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    recordListReturn = [False, [[None for __ in range(4)] for _ in range(4)]]
    recordList = [recordListInput[0][1][0]]

    for i in range(3, 0, -1):
        recordList.append(recordListInput[i][3][0])
        recordList.append(recordListInput[i][1][0])

    recordList.append(recordListInput[0][3][0])

    if ("Green" in recordList):
        green = recordList.index("Green")
    else:
        green = 999

    if ("Red" in recordList):
        red = recordList.index("Red")
    else:
        red = 999

    try:
        if (red < green):
            # UTURN

            print("LAST: RED")

            recordListReturn[0] = True
            
            for i in range(0, -4, -1):
                for j in range(4):
                    recordListReturn[1][abs(i)][j] = recordListInput[i][(j + 2) % 4]

            if (robotDirection == 1):
                # UTURN CLOCKWISE

                monke.driveMotor.control.limits(acceleration= 800)
                monke.street(-80, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.turn(-1, -92, 40, 850, 600)
                monke.look(LEFT, False)
                monke.street(-100, -92, 500, 300)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(150, -90, 2000, 2000)
                monke.fastAcceleration(True)
                monke.streetStall(100, -90, 850, 800, 100)

            else:
                # UTURN COUNTERCLOCKWISE

                monke.driveMotor.control.limits(acceleration= 800)
                monke.street(-20, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.turn(-1, 92, 40, 850, 600)
                monke.look(RIGHT, False)
                monke.street(-100, 92, 500, 300)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(150, 90, 2000, 2000)
                monke.fastAcceleration(True)
                monke.streetStall(200, 90, 850, 800, 100)

        else:
            # NO UTURN

            print("LAST: GREEN")
            recordListReturn[1] = recordListInput
        
        return recordListReturn

    finally:
        monke.motorClose()

if __name__ == "__main__":
    try:
        robotDirection = 1
        _recordListMain = [["-",  ["Red", 1],    "---",  ["Green", 2]], 
                           ["-",  ["Green", 3],    "---",  ["Green", 4]], 
                           ["-",  ["Green", 5],    "---",  ["Green", 6]], 
                           ["-",  ["Green", 7],    "---",  ["Green", 8]]]

        _clock = StopWatch()
        obstacleUTurn(robotDirection, _recordListMain)

        print(f"Time: {_clock.time()}")

        while True: 
            pass

    finally:
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        s.run_target(1000, 0, Stop.HOLD, False)
        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

        if (robotDirection == 1):
            v.run_target(1000, RIGHT, Stop.HOLD, False)
        else:
            v.run_target(1000, LEFT, Stop.HOLD, False)

        wait(800)
