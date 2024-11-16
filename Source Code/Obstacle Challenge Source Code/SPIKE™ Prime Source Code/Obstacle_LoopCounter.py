from FE_Functions import *

def obstacleLoopCounter(recordListInput):
    driveMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 500);
    steerMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1], False, 5);
    visionMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5);
    
    selfDrivingCar = FutureEngineers(steerMotor, driveMotor, visionMotor);

    parkingPresence, trafficSign, recordListValue = "", "", [];

    timer.reset();
    visionMotor.run_target(1000, -100, Stop.HOLD, False);

    if (recordListInput == ["", "", "", ""]):
        parkingPresence = ifParking(650, 280);
        recordListValue.append(parkingPresence);
        print("n" + parkingPresence, end = " ");
    else:
        parkingPresence = recordListInput[0];

    selfDrivingCar.street(-400, 0, 650, 600);
    trafficSign = selfDrivingCar.streetDetect(-100, 0, 600); # dapat ay total of -500

    if (recordListInput == ["", "", "", ""]):
        if (trafficSign == "None"):
            print("false n", end = " ");
            trafficSign = trafficSignColor();

        recordListValue.append(trafficSign);
        print("n" + trafficSign, end = " ");
    else:
        trafficSign = recordListInput[1];

    if (trafficSign == "Green"):
        # nNormal nGreen
        # nParking nGreen

        selfDrivingCar.smartStop(0);
        selfDrivingCar.street(50, 0, 300, 290);
        driveMotor.hold();
        visionMotor.run_target(1000, 0, Stop.HOLD, False);
        selfDrivingCar.turn(-1, -76, 65, 900, 550);
        selfDrivingCar.streetStall(-100, -90, 700, 650, 800);
        selfDrivingCar.street(1050, 0, 900, 750);

        if (recordListInput == ["", "", "", ""] or recordListInput[3] == "Red"):
            visionMotor.run_target(1000, -100, Stop.HOLD, False);
            selfDrivingCar.turn(1, 95, 30, 850, 750);
            selfDrivingCar.streetStall(250, 90, 750, 500, 500);

            if (recordListInput == ["", "", "", ""]):
                if (parkingPresence == "Normal"):
                    parkingPresence = ifParking(600);
                    parkingPresenceBypass = 0;
                else:
                    parkingPresence = "Normal";
                    parkingPresenceBypass = 1;

                recordListValue.append(parkingPresence);
                print("f" + parkingPresence, end = " ");

            else:
                if (parkingPresence == "Normal"):
                    parkingPresenceBypass = 0;
                else:
                    parkingPresenceBypass = 1;

                parkingPresence = recordListInput[2];

            selfDrivingCar.street(-350, -6, 800, 600);
            trafficSign = selfDrivingCar.streetDetect(-180, 0, 600); # dapat ay total of -530

            if (recordListInput == ["", "", "", ""]):
                if (trafficSign == "None"):
                    print("false", end = " ");
                    trafficSign = trafficSignColor();
                
                recordListValue.append(trafficSign);
                print("f" + trafficSign);
            else:
                trafficSign = recordListInput[3];

            if (trafficSign == "Green" or trafficSign == "None"):
                # nNormal nGreen fNormal fGreen
                # nParking nGreen fNormal fGreen
                # nNormal nGreen fParking fGreen

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(-1, -86, 55, 900, 450);
                selfDrivingCar.smartStop(-90);
                selfDrivingCar.streetLine(700, -90, 900, 850);

        else:
            # nNormal nGreen f? fGreen/None
            # nParking nGreen f? fGreen/None

            selfDrivingCar.street(60, -15, 800, 750);
            selfDrivingCar.streetLine(350, 0, 900, 850);
            hub.imu.reset_heading(-90);

        if (trafficSign == "Green" or trafficSign == "None"):
            selfDrivingCar.turn(1, -50, 30, 850, 550);
            selfDrivingCar.street(250, -50, 850, 750);
            visionMotor.run_target(1000, -100, Stop.HOLD, False);
            selfDrivingCar.turn(1, -90, 30, 750, 550);
            selfDrivingCar.streetStall(10, -90, 550, 500, 500);

        else:
            # nNormal nGreen f? fRed
            # nParking nGreen f? fRed

            if ((parkingPresence == "Parking") or parkingPresenceBypass):
                # nParking nGreen fNormal fRed
                # nNormal nGreen fParking fRed

                # selfDrivingCar.street(-100, 0, 620, 600);
                driveMotor.hold();
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(1, -90, 30, 750, 450);
                selfDrivingCar.streetLine(600, -90, 900, 850);

                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.street(400, -130, 800, 750);
                selfDrivingCar.streetStall(200, -90, 750, 600, 500);

            else:
                # nNormal nGreen fNormal fRed

                selfDrivingCar.street(-10, 0, -450, -400);
                driveMotor.hold();
                selfDrivingCar.street(140, 0, 900, 850);
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(1, -85, 30, 850, 750);
                selfDrivingCar.drive(500, 950, 850, 8, -4);
                selfDrivingCar.turn(1, -130, 30, 850, 750);
                selfDrivingCar.street(600, -130, 850, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, -90, 40, 750, 550);
                selfDrivingCar.streetStall(10, -90, 550, 500, 400);

    else:
        # n? nRed

        if (parkingPresence == "Parking"):
            # nParking nRed

            if (recordListInput == ["", "", "", ""]):
                recordListValue.append("Normal");
                print("fNormal", end = " ");

            selfDrivingCar.street(-50, 0, 600, 550);
            driveMotor.hold();
            visionMotor.run_target(1000, 0, Stop.HOLD, False)
            selfDrivingCar.turn(1, -90, 30, 750, 650);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, -90, 650, 550);
            driveMotor.hold();

            visionMotor.run_target(1000, -15, Stop.HOLD, False)
            selfDrivingCar.street(500, -90, 750, 650);

            if (recordListInput == ["", "", "", ""]):
                trafficSign = trafficSignColor();
                trafficSign = "None";
                recordListValue.append(trafficSign);
                print("f" + trafficSign, end = " ");
            else:
                trafficSign = recordListInput[3];

            if (trafficSign == "Green"):
                # nParking nRed fNormal fGreen
                print("");
                
                visionMotor.run_target(1000, 0, Stop.HOLD, False)
                # selfDrivingCar.street(500, -180, 800, 600);
                # selfDrivingCar.streetStall(100, -180, 500, 300, 400);
                selfDrivingCar.turnDuration(490, -180, 30, 700, 550);
                selfDrivingCar.streetStall(100, -180, 350, 300, 400);

                selfDrivingCar.street(-250, 0, 750, 650);
                driveMotor.hold();
                selfDrivingCar.turn(1, 90, 30, 850, 750);
                selfDrivingCar.streetLine(200, 90, 900, 850);

                selfDrivingCar.turn(1, 120, 30, 850, 750);
                selfDrivingCar.street(150, 120, 850, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 30, 750, 550);
                selfDrivingCar.streetStall(100, 90, 550, 500, 500);

            elif (trafficSign == "Red"):
                # nParking nRed fNormal fRed
                print("");

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(370, -90, 900, 850);
                selfDrivingCar.turn(1, -60, 30, 750, 650);
                selfDrivingCar.street(70, -60, 750, 750);
                selfDrivingCar.turn(1, -90, 30, 750, 650);
                selfDrivingCar.street(300, -90, 850, 750);
                selfDrivingCar.turn(1, -130, 30, 850, 750);

                selfDrivingCar.street(200, -130, 850, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, -90, 30, 850, 650);
                selfDrivingCar.streetStall(200, -90, 650, 500, 400);

            else:
                # nParking nRed fNormal false fNone

                selfDrivingCar.street(230, -90, 900, 850);

                trafficSign = trafficSignColor();
                recordListValue[3] = trafficSign;
                print("false f" + trafficSign);

                if (trafficSign == "Green"):
                    # nParking nRed fNormal false fGreen

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(300, -90, 900, 850);
                    # selfDrivingCar.street(500, -180, 800, 600);
                    # selfDrivingCar.streetStall(100, -180, 500, 300, 400);
                    selfDrivingCar.turnDuration(490, -180, 30, 700, 550);
                    selfDrivingCar.streetStall(100, -180, 350, 300, 400);

                    selfDrivingCar.street(-250, 0, 750, 650);
                    driveMotor.hold();
                    selfDrivingCar.turn(1, 120, 30, 850, 750);
                    selfDrivingCar.street(150, 120, 850, 750);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 750, 550);
                    selfDrivingCar.streetStall(100, 90, 550, 500, 500);

                else:
                    # nParking nRed fNormal false fRed

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(70, -90, 760, 750);
                    selfDrivingCar.turn(1, -60, 30, 750, 650);
                    selfDrivingCar.street(70, -60, 750, 750);
                    selfDrivingCar.turn(1, -90, 30, 750, 650);
                    selfDrivingCar.street(300, -90, 850, 750);
                    selfDrivingCar.turn(1, -120, 30, 850, 750);

                    selfDrivingCar.street(300, -120, 850, 750);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 850, 650);
                    selfDrivingCar.streetStall(200, -90, 650, 500, 400);

        else:
            # nNormal nRed

            driveMotor.hold();
            selfDrivingCar.street(120, 0, 850, 800);
            visionMotor.run_target(1000, -3, Stop.HOLD, False);
            selfDrivingCar.turn(1, -91, 30, 800, 600);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, -91, 700, 550);
            driveMotor.hold();
            
            selfDrivingCar.drive(670, 850, 750, 8, -4);

            if (recordListInput == ["", "", "", ""]):
                driveMotor.hold();
                visionMotor.run_target(1000, (-90 - hub.imu.heading()), Stop.HOLD, True);

                distanceLowest = 2000;
                timer.reset();

                while (timer.time() < 200):
                    if (distanceSensor.distance() < distanceLowest):
                        distanceLowest = distanceSensor.distance();

                if (recordListInput == ["", "", "", ""]):
                    if (distanceLowest < 1400):
                        parkingPresence = "Parking";
                    else:
                        parkingPresence = "Normal"

                    recordListValue.append(parkingPresence);
                    print("f" + parkingPresence, end = " ");
                else:
                    parkingPresence = recordListInput[2];

            try:
                conditionTemporary = (recordListInput == ["", "", "", ""] or not(recordListInput[3] == "Red" and recordListInput[2] == "Normal"));
            except:
                conditionTemporary = True;

            if (conditionTemporary):
                selfDrivingCar.turn(1, -180, 30, 850, 750);
                driveMotor.hold();
                selfDrivingCar.streetStall(-350, -180, 900, 850, 800);

                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.street(370, 0, 800, 600);
                trafficSign = selfDrivingCar.streetDetect(130, 0, 600); # dapat ay total of 500
            else:
                pass;

            if (recordListInput == ["", "", "", ""]):
                if (trafficSign == "None"):
                    print("false", end = " ");
                    trafficSign = trafficSignColor();

                recordListValue.append(trafficSign);
                print("f" + trafficSign);
            else:
                trafficSign = recordListInput[3];

            if (trafficSign == "Green"):
                # nNormal nRed fNormal fGreen
                # nNormal nRed fParking fGreen

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 35, 750, 650);
                selfDrivingCar.streetLine(300, 90, 900, 850);

                selfDrivingCar.turn(1, 130, 30, 850, 750);
                selfDrivingCar.street(120, 130, 850, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 30, 750, 550);
                selfDrivingCar.streetStall(100, 90, 650, 550, 500);

            else:
                # nNormal nRed f? fRed

                if (parkingPresence == "Parking"):
                    # nNormal nRed fParking fRed

                    driveMotor.hold();
                    selfDrivingCar.streetStall(-400, 0, 800, 750, 500);
                    
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(50, 0, 650, 650);
                    selfDrivingCar.turn(1, 90, 30, 650, 550);
                    selfDrivingCar.street(700, 90, 900, 850);
                    selfDrivingCar.turn(1, 55, 30, 850, 750);
                    selfDrivingCar.street(40, 55, 750, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 850, 750);
                    selfDrivingCar.streetStall(150, 90, 650, 550, 500);

                else:
                    # nNormal nRed fNormal fRed

                    if (conditionTemporary == True):
                        driveMotor.hold();
                        selfDrivingCar.street(-260, 0, 900, 800);
                        visionMotor.run_target(1000, 0, Stop.HOLD, False);
                        selfDrivingCar.turn(-1, 86, 55, 900, 450);
                        selfDrivingCar.smartStop(90);
                    else:
                        hub.imu.reset_heading(90);

                    selfDrivingCar.drive(1100, 950, 850, 6, -2);
                    selfDrivingCar.turn(1, 45, 30, 850, 750);
                    selfDrivingCar.street(560, 45, 800, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 850, 550);
                    selfDrivingCar.streetStall(100, 90, 600, 550, 600);

    selfDrivingCar.motorClose();

    if (recordListValue == []):
        return recordListInput;
    else:    
        return recordListValue;

# try:
#     recordListValue = ["", "", "", ""];
#     for i in range (2):
#         print("\n");
#         hub.imu.reset_heading(0);
#         recordListValue = obstacleLoopCounter(recordListValue);
# except:
#     pass;
# finally:
#     print(recordListValue);
#     print(timer.time());