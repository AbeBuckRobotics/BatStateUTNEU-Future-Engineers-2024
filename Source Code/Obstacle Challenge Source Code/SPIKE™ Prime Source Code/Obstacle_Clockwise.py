from FE_Functions import *

def nNormalnGreenfRed(monke):
    monke.fastAcceleration(False)
    monke.street(50, 0, 1000, 1000)
    monke.fastAcceleration(True)
    monke.look(0, False)
    monke.turn(1, -35, 40, 2000, 2000)
    monke.street(465, -35, 2000, 2000)
    monke.turn(1, -90, 40, 2000, 2000)
    monke.streetLine(1, -90, 2000, 2000)

    monke.turn(1, -160, 40, 2000, 2000)
    monke.street(150, -160, 2000, 2000)
    monke.look(RIGHT, False)
    monke.turn(1, -90, 40, 1000, 750)
    monke.streetStall(100, -90, 2000, 2000, 100)

def obstacleClockwise(recordListInput, robotLaps):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    parking, trafficSign, recordListValue = "", "", []

    try:
        hub.imu.reset_heading(0)
        clock.reset()
        monke.look(RIGHT, False)

        monke.driveMotor.control.limits(acceleration= 800)
        parking = monke.STREETREAD(-100, 0, 2000, 850, recordListInput[0], recordListValue, "n")
        monke.look(100, False)
        monke.fastAcceleration(True)
        monke.street(-150, 0, 2000, 2000)

        trafficSign = monke.STREETSCAN(-170, 0, 8550, recordListInput[1], recordListValue, "n")

        if (trafficSign[0] == "Green"):
            # n? nGreen

            if (parking == "Parking"):
                # nParking nGreen fNormal

                parking = RECORDPARKING(0, 0, recordListInput[2], recordListValue, "f", fixed = "Normal")
                
                monke.fastAcceleration(True)
                monke.street(-430, 0, 700, 350)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(130, 0, 2000, 2000)
                monke.look(0, False)
                monke.fastAcceleration(True)
                monke.turn(1, 90, 40, 2000, 2000)
                monke.street(100, 90, 2000, 2000)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.streetLine(-10, 90, 850, 600)
                monke.street(-100, 90, 600, 450)

                monke.look(8, False)
                monke.fastAcceleration(False)
                monke.streetLine(1, 90, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(400, 90, 2000, 2000)

                trafficSign = RECORDTRAFFICSIGN(recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Red"):
                    # nParking nGreen fNormal fRed

                    monke.look(0, False)
                    monke.fastAcceleration(True)
                    monke.street(600, 91, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turnSemi(1, 0, -10, 40, 600, 400)
                    monke.streetStall(1, 0, 1000, 1000, 300)

                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.street(-250, 0, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.street(-250, 0, 2000, 2000)
                    monke.look(0, False)
                    monke.turn(-1, 92, 50, 850, 600)
                    monke.street(-100, 92, 500, 300)
                    monke.HOLD(100)

                    monke.fastAcceleration(False)
                    monke.street(150, 90, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.streetLine(100, 90, 2000, 2000)

                    monke.turn(1, 40, 40, 2000, 2000)
                    monke.street(350, 40, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turn(1, 90, 40, 1000, 750)
                    monke.streetStall(10, 90, 850, 2000, 100)

                else:
                    # nParking nGreen fNormal fGreen
                    
                    monke.look(0, False)
                    monke.fastAcceleration(True)
                    monke.street(400, 90, 2000, 2000)
                    monke.street(500, 70, 2000, 2000)
                    monke.street(450, 90, 2000, 2000)
                    monke.street(250, 110, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.streetStall(650, 90, 2000, 2000, 100)

            else:
                # nNormal nGreen

                monke.fastAcceleration(True)
                monke.street(-300, 0, 700, 400)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(230, 0, 2000, 2000)
                monke.look(0, False)
                monke.turn(1, 87, 40, 850, 750)
                monke.HOLD()

                monke.fastAcceleration(False)
                monke.streetLine(-100, 100, 850, 600)
                monke.street(-200, 85, 600, 400)
                monke.HOLD()

                monke.fastAcceleration(False)
                monke.driveLine(1, 2000, 2000, -5, -5)
                monke.fastAcceleration(True)
                monke.drive(550, 2000, 2000, -3, -3)

                if (recordListInput[2] == "Parking"):
                    monke.drive(100, 2000, 2000, -3, -3)
                else:
                    monke.HOLD()
                
                parking = RECORDPARKING(700, 200, recordListInput[2], recordListValue, "f")

                if (parking == "Parking"):
                    # nNormal nGreen fParking 
                    
                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.look(LEFT, False)
                    monke.turn(1, 179, 40, 850, 750)
                    monke.fastAcceleration(True)
                    
                    trafficSign = monke.STREETSCAN(150, 180, 2000, recordListInput[3], recordListValue, "f")
                    monke.HOLD()

                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.street(-100, 180, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.streetStall(-250, 180, 700, 900, 200)

                    if (trafficSign[0] == "Red"):
                        # nNormal nGreen fParking fRed

                        nNormalnGreenfRed(monke)

                    else:
                        # nNormal nGreen fParking fGreen

                        monke.driveMotor.control.limits(acceleration=800)
                        monke.look(0, False)
                        monke.turn(1, -90, 30, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetLine(600, -90, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.streetStall(500, -90, 2000, 2000, 100)

                else:
                    # nNormal nGreen fNormal 

                    trafficSign = monke.CAMERASCAN(20, 40, 100, recordListInput[3], recordListValue, "f")

                    if (trafficSign[0] == "Red"): 
                        # nNormal nGreen fNormal fRed

                        monke.fastAcceleration(False)
                        monke.drive(100, 2000, 2000, -1, -1)
                        monke.look(LEFT, False)
                        monke.fastAcceleration(True)
                        monke.turn(1, 181, 40, 850, 750)
                        monke.HOLD()
                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, 180, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetStall(-250, 180, 600, 850, 200)

                        nNormalnGreenfRed(monke)

                    else:
                        # nNormal nGreen fNormal fGreen
                        
                        monke.look(0, False)
                        monke.fastAcceleration(False)
                        monke.drive(100, 2000, 2000, -3, -3)
                        monke.fastAcceleration(True)
                        monke.drive(950, 2000, 2000, -3, -1)

                        # monke.street(1000, 110, 2000, 2000)
                        monke.turn(1, 120, 40, 2000, 2000)
                        monke.street(450, 120, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.streetStall(500, 90, 2000, 2000, 100)
            
        

        else:
            # n? nRed

            monke.fastAcceleration(True)
            monke.street(-50, 0, 2000, 2000)
            monke.look(0, False)
            monke.turn(-1, 90, 40, 900, 750)
            monke.streetStall(-10, 90, 2000, 500, 200)

            monke.fastAcceleration(False)
            monke.street(100, 0, 2000, 2000)
            monke.fastAcceleration(True)
            monke.street(950, 0, 2000, 2000)
            
            if (parking == "Parking"):
                # nParking nRed fNormal

                parking = RECORDPARKING(0, 0, recordListInput[0], recordListValue, "f", fixed = "Normal")

                monke.look(-30, False)
                monke.fastAcceleration(True)
                monke.street(600, 0, 2000, 2000)

                trafficSign = RECORDTRAFFICSIGN(recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Green"):
                    # nParking nRed fNormal fGreen

                    monke.look(0, False)
                    monke.turnSemi(1, -60, -70, 40, 2000, 2000)
                    monke.street(260, -70, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turnSemi(1, 0, 5, 40, 2000, 2000)
                    monke.streetStall(850, 0, 2000, 2000, 100)

                else:
                    # nParking nRed fNormal fRed

                    monke.look(0, False)
                    monke.fastAcceleration(True)
                    monke.streetLine(350, 0, 2000, 2000)

                    monke.turn(1, -60, 40, 2000, 2000)
                    monke.street(320, -60, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turn(1, 0, 40, 1000, 750)
                    monke.streetStall(10, 0, 750, 700, 100)

            else:
                # nNormal nRed

                monke.look(RIGHT, False)
                monke.fastAcceleration(True)
                monke.turn(1, -90, 40, 2000, 2000)
                monke.streetStall(380, -90, 900, 800, 200)

                monke.driveMotor.control.limits(acceleration= 800)
                parking = monke.STREETREAD(-100, 0, 2000, 1000, recordListInput[2], recordListValue, "f")
                monke.look(100, False)
                monke.fastAcceleration(True)
                monke.street(-150, 0, 2000, 2000)

                trafficSign = monke.STREETSCAN(-170, 0, 950, recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Green"):
                    # nNormal nRed f? fGreen

                    if (parking == "Parking"):
                        # nNormal nRed fParking fGreen

                        monke.fastAcceleration(True)
                        monke.street(-430, 0, 700, 350)
                        monke.HOLD(100)

                        monke.fastAcceleration(False)
                        monke.street(130, 0, 2000, 2000)
                        monke.look(0, False)
                        monke.fastAcceleration(True)
                        monke.turn(1, 90, 40, 2000, 2000)
                        monke.streetLine(700, 90, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.streetStall(500, 90, 2000, 1000, 100)
                    
                    else: 
                        # nNormal nRed fNormal fGreen

                        monke.fastAcceleration(True)
                        monke.street(-150, 0, 400, 300)
                        monke.HOLD(100)
                        
                        monke.fastAcceleration(False)
                        monke.street(200, 0, 2000, 2000)
                        monke.look(0, False)
                        monke.fastAcceleration(True)
                        monke.turn(1, 88, 40, 2000, 2000)
                        monke.street(650, 80, 2000, 2000)

                        monke.street(700, 120, 2000, 2000)
                        monke.look(RIGHT, False)
                        monke.streetStall(200, 90, 2000, 2000, 200)

                else:
                    # nNormal nRed fParking fRed
                    # nNormal nRed fNormal fRed

                    monke.look(0, False)
                    monke.fastAcceleration(True)
                    monke.street(-50, 0, 2000, 2000)
                    monke.turn(-1, 92, 40, 850, 750)
                    monke.street(-100, 92, 500, 300)
                    monke.HOLD(100)

                    monke.fastAcceleration(False)
                    monke.street(150, 90, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.streetLine(650, 90, 2000, 2000)

                    monke.turn(1, 30, 40, 2000, 2000)
                    monke.street(280, 30, 2000, 2000)
                    monke.look(RIGHT, False)
                    monke.turn(1, 90, 40, 1000, 750)
                    monke.streetStall(50, 90, 750, 700, 100)

    finally: 
        monke.motorClose()

    if (recordListValue == []):
        return recordListInput
    else:
        return recordListValue

if __name__ == "__main__":
    try:
        print(hub.battery.voltage())
        hub.speaker.beep(500)

        recordListValue = [None for x in range(4)]
        _ = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        _.run_target(1000, 90, Stop.HOLD, False)
        wait(800)
        _.close()

        _ = 0

        for i in range(4):
            print("\n")
            recordListValue = [None for x in range(4)]
            hub.imu.reset_heading(0)
            recordListValue = obstacleClockwise(recordListValue, _)
            print(f"Time: {clock.time()}")

    finally:
        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        v.run_target(1000, 90, Stop.HOLD, False)
        s.run_target(1000, 0, Stop.HOLD, False)
        wait(800)
