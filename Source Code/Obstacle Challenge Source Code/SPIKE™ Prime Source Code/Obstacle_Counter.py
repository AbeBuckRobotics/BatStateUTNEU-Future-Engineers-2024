from FE_Functions import *

def nNormalnRedfGreen(monke):
    monke.fastAcceleration(False)
    monke.street(150, 0, 1000, 1000)
    monke.look(0, False)
    monke.fastAcceleration(True)
    monke.street(650, 35, 2000, 2000)
    monke.turn(1, 90, 40, 2000, 2000)
    monke.streetLine(1, 90, 2000, 2000)

    monke.turn(1, 140, 40, 2000, 2000)
    monke.street(180, 140, 2000, 2000)
    monke.look(LEFT, False)
    monke.turn(1, 90, 40, 1000, 750)
    monke.streetStall(150, 90, 750, 700, 100)

def nGreenfGreen(monke):
    monke.look(0, False)
    monke.fastAcceleration(True)
    monke.streetLine(350, 0, 2000, 2000)

    monke.turn(1, 50, 40, 2000, 2000)
    monke.street(100, 50, 2000, 2000)
    monke.look(LEFT, False)
    monke.turn(1, 0, 40, 1000, 750)
    monke.streetStall(200, 0, 750, 700, 100)

def obstacleCounter(recordListInput, robotLaps):
    driveMotor = Motor(Port.A, Direction.CLOCKWISE, [1], False, 500)
    steerMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
    visionMotor = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)

    monke = FutureEngineers(driveMotor, steerMotor, visionMotor)

    parking, trafficSign, recordListValue = "", "", []

    try:
        hub.imu.reset_heading(0)
        clock.reset()
        monke.look(LEFT, False)

        # fast route    nred parking s1

        if (not ((recordListInput[0] == "Parking" or recordListInput[2] == "Parking") and recordListInput[1][0] == "Red")):
            monke.driveMotor.control.limits(acceleration= 800)
            parking = monke.STREETREAD(-100, 0, 2000, 750, recordListInput[0], recordListValue, "n")
            monke.look(-100, False)
            monke.fastAcceleration(True)
            monke.street(-150, 0, 2000, 2000)

            trafficSign = monke.STREETSCAN(-170, 0, 950, recordListInput[1], recordListValue, "n")

        else:
            parking = RECORDPARKING(0, 0, recordListInput[0], recordListValue, "n")
            trafficSign = RECORDTRAFFICSIGN(recordListInput[1], recordListValue, "n")

        if (trafficSign[0] == "Red"):
            # n? nRed

            if (parking == "Parking" or recordListInput[2] == "Parking"):
                # nParking nRed fNormal

                parking = RECORDPARKING(0, 0, recordListInput[2], recordListValue, "f", fixed = "Normal")

                # fast route    nred parking s2
                
                if (not ((recordListInput[0] == "Parking" or recordListInput[2] == "Parking") and recordListInput[1][0] == "Red")):
                    monke.street(-100, 0, 400, 300)
                    monke.HOLD(100)

                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.street(50, 0, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.streetStall(300, 0, 900, 900, 100)

                monke.driveMotor.control.limits(acceleration= 800)
                monke.street(-50, 0, 2000, 2000)
                monke.look(0, False)
                monke.fastAcceleration(True)
                monke.turn(-1, -90, 50, 850, 600)
                monke.streetStall(-200, -90, 2000, 500, 100)
                
                monke.fastAcceleration(False)
                monke.streetLine(200, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(400, 0, 2000, 2000)

                if (recordListInput[3] == None):
                    monke.HOLD(100)

                trafficSign = monke.CAMERASCAN(0, -10, 100, recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Green"):
                    # nParking nRed fNormal fGreen
                    # nParking nRed fGreen

                    monke.fastAcceleration(False)
                    monke.turn(1, -60, 40, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.street(150, -60, 2000, 2000)
                    monke.turn(1, 0, 40, 2000, 2000)
                    monke.streetLine(300, 0, 2000, 2000)

                    monke.turn(1, 50, 40, 2000, 2000)
                    monke.street(100, 50, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.turn(1, 0, 40, 1000, 750)
                    monke.streetStall(200, 0, 750, 700, 100)

                else:
                    # nParking nRed fNormal fRed
                    # nParking nRed fRed

                    monke.look(0, False)
                    monke.street(150, 0, 2000, 2000)
                    monke.fastAcceleration(True)
                    monke.streetLine(800, -1, 2000, 2000)
                    monke.street(250, -65, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.streetStall(300, 0, 2000, 900, 100)
                
            else: 
                # nNormal nRed

                monke.fastAcceleration(True)
                monke.street(-270, 0, 700, 400)
                monke.HOLD(100)

                monke.fastAcceleration(False)
                monke.street(100, 0, 2000, 2000)
                monke.fastAcceleration(True)
                monke.street(230, 0, 2000, 2000)
                monke.look(0, False)
                monke.turn(1, -87, 40, 850, 750)
                monke.HOLD()

                monke.fastAcceleration(False)
                monke.streetLine(-100, -100, 850, 700)
                monke.street(-150, -85, 700, 450)
                monke.HOLD()

                monke.driveMotor.control.limits(acceleration= 800)
                monke.driveLine(1, 2000, 2000, 5, 5)
                monke.fastAcceleration(True)
                monke.drive(550, 2000, 2000, 3, 3)

                # fast route    nNormal nRed f?

                if (recordListInput[2] == "Parking"):
                    monke.drive(100, 2000, 2000, 3, 3)
                elif (recordListInput[2] == "Normal"):
                    monke.drive(100, 2000, 2000, 3, 3)
                else:
                    monke.HOLD()
                
                parking = RECORDPARKING(700, 200, recordListInput[2], recordListValue, "f")

                if (parking == "Parking"):
                    # nNormal nRed fParking 
                    
                    monke.driveMotor.control.limits(acceleration= 800)
                    monke.look(RIGHT, False)
                    monke.turn(1, -179, 40, 850, 750)

                    # fast route    nNormal nRed fParking f?

                    if (recordListInput[3] == None):
                        monke.fastAcceleration(True)
                        trafficSign = monke.STREETSCAN(150, -180, 2000, recordListInput[3], recordListValue, "f")
                        monke.HOLD()
                        
                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, -180, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetStall(-250, -180, 700, 900, 200)

                    else:
                        trafficSign = RECORDTRAFFICSIGN(recordListInput[3], recordListValue, "f")

                        monke.HOLD()
                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-100, -180, 800, 900)
                        monke.fastAcceleration(True)
                        monke.streetStall(-100, -180, 850, 800, 200)

                    if (trafficSign[0] == "Green"):
                        # nNormal nRed fParking fGreen

                        nNormalnRedfGreen(monke)

                    else:
                        # nNormal nRed fParking fRed 

                        monke.look(0, False)
                        monke.driveMotor.control.limits(acceleration=800)
                        monke.street(50, 0, 2000, 2000)
                        monke.turn(1, 90, 40, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetLine(600, 90, 2000, 2000)

                        monke.turn(1, 60, 40, 2000, 2000)
                        monke.look(LEFT, False)
                        monke.streetStall(150, 90, 2000, 1000, 100)

                else:
                    # nNormal nRed fNormal

                    trafficSign = monke.CAMERASCAN(-20, -40, 100, recordListInput[3], recordListValue, "f")

                    if (trafficSign[0] == "Green"): 
                        # nNormal nRed fNormal fGreen
                        # nRed fGreen

                        monke.fastAcceleration(False)
                        monke.drive(100, 2000, 2000, 1, 1)
                        monke.look(RIGHT, False)
                        monke.fastAcceleration(True)
                        monke.turn(1, -181, 40, 850, 750)
                        monke.HOLD()

                        monke.driveMotor.control.limits(acceleration= 800)
                        monke.street(-50, -180, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetStall(-250, -180, 700, 800, 200)

                        nNormalnRedfGreen(monke)

                    else:
                        # nNormal nRed fNormal fRed
                        # nRed fRed
                        
                        monke.look(0, False)
                        monke.fastAcceleration(False)
                        monke.drive(100, 2000, 2000, 3, 3)
                        monke.fastAcceleration(True)
                        monke.drive(1100, 2000, 2000, 3, 1)

                        monke.street(630, -160, 2000, 2000)
                        monke.look(LEFT, False)
                        monke.streetStall(700, -90, 2000, 2000, 100)



        else:
            # n? nGreen

            monke.fastAcceleration(True)
            monke.street(-30, 0, 2000, 2000)
            monke.look(0, False)
            monke.turn(-1, -92, 40, 850, 600)
            monke.streetStall(-200, -90, 2000, 500, 200)

            monke.fastAcceleration(False)
            monke.street(100, 0, 2000, 2000)
            monke.fastAcceleration(True)
            monke.street(950, 0, 2000, 2000)

            if (parking == "Parking"):
                # nParking nGreen fNormal

                parking = RECORDPARKING(0, 0, recordListInput[0], recordListValue, "f", fixed = "Normal")

                monke.look(30, False)
                monke.fastAcceleration(True)
                monke.street(600, 0, 2000, 2000)

                trafficSign = RECORDTRAFFICSIGN(recordListInput[3], recordListValue, "f")

                if (trafficSign[0] == "Red"):
                    # nParking nGreen fNormal fRed
                    # nParking nGreen fRed

                    monke.look(0, False)
                    monke.turnSemi(1, 60, 65, 40, 2000, 2000)
                    monke.street(280, 70, 2000, 2000)
                    monke.turn(1, -50, 40, 2000, 2000)
                    monke.look(LEFT, False)
                    monke.turn(1, 0, 40, 2000, 2000)
                    monke.streetStall(250, 0, 2000, 2000, 100)

                else:
                    # nParking nGreen fNormal fGreen
                    # nParking nGreen fGreen

                    nGreenfGreen(monke)
                    
            else:
                # nNormal nGreen

                # fast route    nGreen fGreen

                if (recordListInput[3] != None and recordListInput[3][0] != "Red"):
                    monke.fastAcceleration(True)
                    monke.street(600, 0, 2000, 2000)

                    nGreenfGreen(monke)

                else:
                    monke.look(LEFT, False)
                    monke.fastAcceleration(True)
                    monke.turn(1, 90, 40, 2000, 800)
                    monke.streetStall(380, 90, 900, 800, 200)

                    monke.driveMotor.control.limits(acceleration= 800)
                    parking = monke.STREETREAD(-100, 0, 2000, 600, recordListInput[2], recordListValue, "f")
                    monke.look(-100, False)
                    monke.fastAcceleration(True)
                    monke.street(-150, 0, 2000, 2000)

                    trafficSign = monke.STREETSCAN(-170, 0, 950, recordListInput[3], recordListValue, "f")

                    if (trafficSign[0] == "Red"):
                        # nNormal nGreen f? fRed

                        if (parking == "Parking"):
                            # nNormal nGreen fParking fRed




                            

                            monke.fastAcceleration(True)
                            monke.street(-380, 0, 700, 350)
                            monke.HOLD(100)

                            monke.fastAcceleration(False)
                            monke.street(130, 0, 800, 2000)
                            monke.look(0, False)
                            monke.fastAcceleration(True)
                            monke.turn(1, -90, 40, 900, 800)
                            monke.streetLine(700, -91, 800, 1000)
                            monke.turn(1, -130, 40, 2000, 2000)
                            monke.look(LEFT, False)
                            monke.streetStall(200, -90, 2000, 1000, 100)

                        else:
                            # nNormal nGreen fNormal fRed
                            # nGreen fRed

                            monke.fastAcceleration(True)
                            monke.street(-150, 0, 400, 300)
                            monke.HOLD()
                            
                            monke.driveMotor.control.limits(acceleration= 800)
                            monke.street(100, 0, 900, 900)
                            monke.fastAcceleration(True)
                            monke.street(100, 0, 2000, 2000)
                            monke.look(0, False)
                            monke.turn(1, -88, 40, 2000, 2000)
                            monke.street(650, -80, 2000, 2000)

                            monke.street(700, -150, 2000, 2000)
                            monke.look(LEFT, False)
                            monke.streetStall(450, -90, 2000, 2000, 200)

                    else: 
                        # nNormal nGreen fParking fGreen
                        # nNormal nGreen fNormal fGreen
                        # nGreen fGreen

                        monke.look(0, False)
                        monke.fastAcceleration(True)
                        monke.street(-30, 0, 2000, 2000)
                        monke.turn(-1, -93, 40, 850, 600)
                        monke.street(-100, -93, 500, 300)
                        monke.HOLD(100)

                        monke.fastAcceleration(False)
                        monke.street(150, -90, 2000, 2000)
                        monke.fastAcceleration(True)
                        monke.streetLine(650, -90, 2000, 2000)

                        monke.turn(1, -40, 40, 2000, 2000)
                        monke.street(100, -40, 2000, 2000)
                        monke.look(LEFT, False)
                        monke.turn(1, -90, 40, 1000, 750)
                        monke.streetStall(100, -90, 750, 700, 100)

                
    finally:
        monke.motorClose()

    if (recordListValue == []):
        return recordListInput
    else:
        return recordListValue



if __name__ == "__main__":
    try:
        print(f"Voltage: {hub.battery.voltage()}")
        hub.speaker.beep(500)

        recordListValue = [None for x in range(4)]
        _ = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        _.run_target(1000, -90, Stop.HOLD, False)
        wait(800)
        _.close()

        _ = 0

        for i in range(4):
            print("\n")
            # recordListValue = [None for x in range(4)]
            hub.imu.reset_heading(0)
            recordListValue = obstacleCounter(recordListValue, _)
            print(f"Time: {clock.time()}")

    finally:
        v = Motor(Port.F, Direction.CLOCKWISE, [1], False, 5)
        s = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 5)
        v.run_target(1000, -90, Stop.HOLD, False)
        s.run_target(1000, 0, Stop.HOLD, False)
        wait(800)
