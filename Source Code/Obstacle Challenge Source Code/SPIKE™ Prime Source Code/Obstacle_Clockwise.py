                          

from FE_Functions import *

def nNormalnGreenfRed(monke):
    monke.fastAcceleration(False)
    monke.street(230, 0, 1000, 1000)
    monke.look(0, False)
    monke.fastAcceleration(True)
    monke.street(600, -35, 2000, 2000)
    monke.turn(1, -90, 40, 2000, 2000)
    monke.streetLine(1, -90, 2000, 2000)

    monke.turn(1, -160, 40, 2000, 2000)
    monke.street(180, -160, 2000, 2000)
    monke.look(RIGHT, False)
    monke.turn(1, -90, 40, 1000, 750)
    monke.streetStall(100, -90, 850, 800, 100)

def nRedfRed(monke):
    monke.look(0, False)
    monke.fastAcceleration(True)
    monke.streetLine(350, 0, 2000, 2000)

    monke.turn(1, -65, 40, 2000, 2000)
    monke.street(320, -65, 2000, 2000)
    monke.look(RIGHT, False)
    monke.turn(1, 0, 40, 1000, 750)
    monke.streetStall(10, 0, 750, 700, 100)

def obstacleClockwise(recordListInput, robotLaps, robotLapsTarget = -1):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)
    monke.start()

    parking, trafficSign, recordListValue = "", "", []

    try:
        hub.imu.reset_heading(0)
        clock.reset()
        monke.look(RIGHT, False)

        # fast route    ngreen parking s1

        if (not ((recordListInput[0] == "Parking" or recordListInput[2] == "Parking") and recordListInput[1][0] == "Green")):
            monke.driveMotor.control.limits(acceleration= 800)
            parking = monke.STREETREAD(-100, 0, 2000, 850, recordListInput[0], recordListValue, "n")
            monke.look(100, False)
            monke.fastAcceleration(True)
            monke.street(-150, 0, 2000, 2000)

            trafficSign = monke.STREETSCAN(-170, 0, 950, recordListInput[1], recordListValue, "n")

        else:
            parking = RECORDPARKING(0, 0, recordListInput[0], recordListValue, "n")
            trafficSign = RECORDTRAFFICSIGN(recordListInput[1], recordListValue, "n")

        if (trafficSign[0] == "Green"):
            # n? nGreen

            if (parking == "Parking" or recordListInput[2] == "Parking"):
                # nParking nGreen fNormal

                parking = RECORDPARKING(0, 0, recordListInput[2], recordListValue, "f", fixed = "Normal")
                
                if (not ((recordListInput[0] == "Parking" or recordListInput[2] == "Parking") and recordListInput[1][0] == "Green")):
                    monke.street(-100, 0, 400, 300)
                    monke.HOLD(100)

                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.street(100, 0, 1000, 900)
                    monke.fastAcceleration(True)
                    monke.streetStall(250, 0, 900, 900, 100)

                monke.driveMotor.control.limits(acceleration= 800)
                monke.street(-30, 0, 850, 850)
                monke.look(0, False)
                monke.fastAcceleration(True)
                monke.turn(-1, 90, 50, 850, 600)
                monke.streetStall(-10, 90, 600, 500, 100)

                monke.fastAcceleration(False)
                monke.streetLine(200, 0, 600, 700)
                monke.street(400, 0, 2000, 2000)

                if (recordListInput[3] == None):
                    monke.HOLD(100)

                trafficSign = monke.CAMERASCAN(0, 10, 100, recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Red"):
                    # nParking nGreen fNormal fRed
                    # nParking nGreen fRed

                    monke.fastAcceleration(False)
                    monke.street(150, 0, 2000, 2000)

                    if (robotLaps == robotLapsTarget):
                        monke.FINISHINGHOLD()
                        monke.driveMotor.control.limits(acceleration= 800)
                    else:
                        monke.fastAcceleration(True)

                    monke.turn(1, 60, 40, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.street(250, 60, 2000, 2000)
                    monke.turn(1, 0, 40, 2000, 2000)
                    monke.streetLine(120, 0, 2000, 2000)

                    monke.turn(1, -60, 40, 2000, 2000)
                    monke.street(350, -60, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turn(1, 0, 40, 850, 750)
                    monke.streetStall(10, 0, 750, 700, 100)

                else:
                    # nParking nGreen fNormal fGreen
                    # nParking nGreen fGreen
                    
                    monke.look(0, False)
                    monke.fastAcceleration(False)
                    monke.street(150, 0, 2000, 2000)

                    if (robotLaps == robotLapsTarget):
                        monke.FINISHINGHOLD()

                    monke.fastAcceleration(False)
                    monke.street(150, -1, 850, 850)
                    monke.fastAcceleration(True)
                    monke.streetLine(550, -1, 850, 850)
                    monke.street(200, -60, 850, 850)
                    monke.look(RIGHT, False)
                    monke.streetStall(250, -1, 2000, 2000, 100)

            else:
                # nNormal nGreen

                monke.fastAcceleration(True)
                monke.street(-220, 0, 700, 400)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(230, 0, 2000, 2000)
                monke.look(0, False)
                monke.turn(1, 87, 40, 850, 750)
                monke.HOLD()

                monke.fastAcceleration(False)
                monke.streetLine(-110, 100, 850, 600)
                monke.street(-200, 85, 600, 450)
                monke.HOLD()

                monke.driveMotor.control.limits(acceleration= 800)
                monke.driveLine(1, 2000, 2000, -5, -5)
                monke.fastAcceleration(True)
                monke.drive(600, 2000, 2000, -3, -3)

                # fast route    nNormal nGreen f?

                if (recordListInput[2] == "Parking"):
                    monke.drive(100, 2000, 2000, -3, -3)
                elif (recordListInput[2] == "Normal"):
                    monke.drive(100, 2000, 2000, -3, -3)
                else:
                    monke.HOLD()
                
                parking = RECORDPARKING(700, 200, recordListInput[2], recordListValue, "f", fixed = "Normal")

                if (parking == "Parking"):
                    # nNormal nGreen fParking 
                    
                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.look(LEFT, False)
                    monke.turn(1, 179, 40, 850, 750)

                    # fast route    nNormal nGreen fParking f?
                    
                    if (recordListInput[3] == None):
                        monke.fastAcceleration(True)
                        trafficSign = monke.STREETSCAN(150, 180, 2000, recordListInput[3], recordListValue, "f")
                        monke.HOLD()

                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, 180, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetStall(-250, 180, 700, 800, 200)

                    else:
                        trafficSign = RECORDTRAFFICSIGN(recordListInput[3], recordListValue, "f")

                        monke.HOLD()
                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, 180, 800, 900)
                        monke.fastAcceleration(True)
                        monke.streetStall(-100, 180, 850, 800, 200)

                    if (trafficSign[0] == "Red"):
                        # nNormal nGreen fParking fRed

                        nNormalnGreenfRed(monke)

                    else:
                        # nNormal nGreen fParking fGreen

                        monke.look(0, False)
                        monke.driveMotor.control.limits(acceleration=800)
                        monke.street(50, 0, 2000, 2000)
                        monke.turn(1, -90, 40, 850, 800)
                        monke.fastAcceleration(True)
                        monke.streetLine(600, -93, 2000, 2000)

                        monke.look(RIGHT, False)
                        monke.streetStall(500, -90, 2000, 2000, 100)

                else:
                    # nNormal nGreen fNormal 

                    trafficSign = monke.CAMERASCAN(3, 35, 100, recordListInput[3], recordListValue, "f")

                    if (trafficSign[0] == "Red"): 
                        # nNormal nGreen fNormal fRed
                        # nGreen fRed

                        monke.fastAcceleration(False)
                        monke.drive(100, 1000, 870, -1, -1)
                        monke.look(LEFT, False)
                        monke.fastAcceleration(True)
                        monke.turn(1, 181, 40, 850, 750)

                        if (robotLaps == robotLapsTarget):
                            monke.FINISHINGHOLD()
                        else:
                            monke.HOLD()

                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, 180, 1000, 900)
                        monke.fastAcceleration(True)
                        monke.streetStall(-100, 180, 600, 500, 200)

                        nNormalnGreenfRed(monke)

                    else:
                        # nNormal nGreen fNormal fGreen
                        # nGreen fGreen
                        
                        monke.look(0, False)
                        monke.fastAcceleration(False)
                        monke.drive(200, 2000, 2000, -3, -3)

                        if (robotLaps == robotLapsTarget):
                            monke.FINISHINGHOLD()
                            monke.driveMotor.control.limits(acceleration= 800)
                            monke.drive(870, 2000, 2000, -3, -1)

                        else:
                            monke.fastAcceleration(True)
                            monke.drive(950, 2000, 2000, -3, -1)

                        # monke.street(1000, 110, 2000, 2000)
                        monke.turn(1, 120, 40, 2000, 2000)
                        monke.street(470, 120, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.streetStall(480, 90, 2000, 2000, 100)
            
        

        else:
            # n? nRed

            monke.fastAcceleration(True)
            monke.street(-100, 0, 2000, 2000)
            monke.look(0, False)
            monke.turn(-1, 90, 40, 900, 750)
            monke.streetStall(-10, 90, 750, 500, 200)

            monke.fastAcceleration(False)
            monke.street(100, 0, 2000, 2000)
            monke.fastAcceleration(True)
            monke.street(950, 0, 2000, 2000)
            
            if (parking == "Parking"):
                # nParking nRed fNormal

                parking = RECORDPARKING(0, 0, recordListInput[0], recordListValue, "f", fixed = "Normal")

                monke.look(-30, False)
                monke.fastAcceleration(True)
                monke.street(250, 0, 2000, 2000)

                if (robotLaps == robotLapsTarget):
                    monke.FINISHINGHOLD()
                    monke.driveMotor.control.limits(acceleration= 800)
                    temp = 30
                else:
                    monke.street(50, 0, 2000, 2000)
                    temp = 0

                trafficSign = monke.STREETSCAN(200 - temp, 0, 2000, recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Green"):
                    # nParking nRed fNormal fGreen
                    # nParking nRed fGreen

                    monke.look(0, False)
                    monke.turnSemi(1, -60, -70, 40, 900, 850)
                    monke.street(310, -70, 900, 1200)
                    monke.look(RIGHT, False)
                    monke.turnSemi(1, 0, 5, 40, 900, 850)
                    monke.streetStall(1000, 0, 1100, 900, 100)

                else:
                    # nParking nRed fNormal fRed
                    # nParking nRed fRed

                    nRedfRed(monke)

            else:
                # nNormal nRed

                # fast route    nRed fRed

                if (recordListInput[3] != None and recordListInput[3][0] != "Green"):
                    monke.fastAcceleration(True)
                    monke.street(250, 0, 2000, 2000)

                    if (robotLaps == robotLapsTarget):
                        monke.FINISHINGHOLD()
                        monke.driveMotor.control.limits(acceleration= 800)
                    else:
                        monke.street(50, 0, 2000, 2000)

                    monke.street(300, 0, 2000, 2000)
                    
                    nRedfRed(monke)

                else:
                    monke.look(RIGHT, False)
                    monke.fastAcceleration(True)
                    monke.street(100, 0, 2000, 2000)
                    monke.turn(1, -90, 40, 2000, 2000)

                    if (robotLaps == robotLapsTarget):
                        monke.FINISHINGHOLD()
                        monke.fastAcceleration(False)
                    else:
                        monke.street(80, -90, 2000, 2000)

                    monke.streetStall(270, -90, 900, 800, 200)

                    monke.driveMotor.control.limits(acceleration= 800)
                    parking = monke.STREETREAD(-100, 0, 2000, 1000, recordListInput[2], recordListValue, "f", fixed = "Normal")
                    monke.look(100, False)
                    monke.fastAcceleration(True)
                    monke.street(-120, 0, 2000, 2000)

                    trafficSign = monke.STREETSCAN(-200, 0, 950, recordListInput[3], recordListValue, "f")

                    if (trafficSign[0] == "Green"):
                        # nNormal nRed f? fGreen

                        if (parking == "Parking"):
                            # nNormal nRed fParking fGreen

                            monke.fastAcceleration(True)
                            monke.street(-370, 0, 700, 350)
                            monke.HOLD(100)

                            monke.fastAcceleration(False)
                            monke.street(150, 0, 800, 2000)
                            monke.look(0, False)
                            monke.fastAcceleration(True)
                            monke.turn(1, 90, 40, 2000, 2000)
                            monke.streetLine(700, 90, 2000, 2000)
                            monke.look(RIGHT, False)
                            monke.streetStall(500, 90, 2000, 1000, 100)
                        
                        else: 
                            # nNormal nRed fNormal fGreen
                            # nRed fGreen

                            monke.fastAcceleration(True)
                            monke.street(-200, 0, 400, 300)
                            monke.HOLD(100)
                            
                            monke.fastAcceleration(False)
                            monke.street(310, 0, 700, 850)
                            monke.look(0, False)
                            monke.fastAcceleration(True)
                            monke.turn(1, 88, 40, 850, 850)
                            monke.street(650, 80, 850, 850)

                            monke.street(700, 120, 850, 900)
                            monke.look(RIGHT, False)
                            monke.streetStall(200, 90, 900, 800, 200)

                    else:
                        # nNormal nRed fParking fRed
                        # nNormal nRed fNormal fRed
                        # nRed fRed

                        monke.look(0, False)
                        monke.fastAcceleration(True)
                        monke.street(-100, 0, 2000, 2000)
                        monke.turn(-1, 92, 40, 850, 750)
                        monke.street(-100, 92, 500, 300)
                        monke.HOLD(100)

                        monke.fastAcceleration(False)
                        monke.street(150, 90, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetLine(550, 90, 2000, 2000)

                        monke.turn(1, 30, 40, 2000, 2000)
                        monke.street(280, 30, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.turn(1, 90, 40, 750, 650)
                        monke.streetStall(10, 90, 650, 600, 100)

    finally: 
        monke.motorClose()

    if (recordListValue == []):
        return recordListInput
    else:
        return recordListValue

        

if __name__ == "__main__":
    hub.speaker.beep(500)
    _ = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
    _.run_target(1000, 90, Stop.HOLD, False)
    wait(800)
    _.close()

    try:
        while True:
            print(hub.battery.voltage())

            recordListValue = [None, None, None, None]
            # recordListValue = ["Parking", "Green", "Normal", "Red"]

            robotLaps = 0
            robotLapsTarget = 10

            for i in range(4):
                robotLaps += 1

                recordListValue = obstacleClockwise(recordListValue, robotLaps, robotLapsTarget)
                print(f"Time: {clock.time()}")

    finally:
        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        v.run_target(1000, RIGHT, Stop.HOLD, False)
        s.run_target(1000, 0, Stop.HOLD, False)
        wait(800)

        v.close()
        s.close()

