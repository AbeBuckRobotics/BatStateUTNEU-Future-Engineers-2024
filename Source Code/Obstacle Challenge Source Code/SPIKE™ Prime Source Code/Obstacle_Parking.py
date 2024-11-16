from FE_Functions import *

def obstacleParking(obstacleParkingDirection, recordListInput):
    driveMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 500);
    steerMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1], False, 5);
    visionMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5);
    
    selfDrivingCar = FutureEngineers(steerMotor, driveMotor, visionMotor);

    visionMotor.run_target(1000, 0, Stop.HOLD, False);
    hub.imu.reset_heading(0);

    if (obstacleParkingDirection == 1): # CLOCKWISE
        if (recordListInput[1][0] == "Parking"):
            # nParking Start

            selfDrivingCar.street(-600, 0, 750, 650);
            driveMotor.hold();
            selfDrivingCar.turn(1, 88, 30, 850, 750);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, 92, 650, 550);
            driveMotor.hold();

            selfDrivingCar.street(370, 90, 850, 800);
            selfDrivingCar.drive(170, 850, 650, -35, -35);
            driveMotor.hold();

        else:
            selfDrivingCar.street(-250, 0, 750, 650);
            driveMotor.hold();
            selfDrivingCar.turn(1, 88, 30, 850, 750);

            if (recordListInput[1][2] == "Parking"):
                driveMotor.hold();
                selfDrivingCar.streetLine(-100, 90, 750, 650);
                driveMotor.hold();
                selfDrivingCar.drive(680, 1000, 1000, -10, -5);
                selfDrivingCar.turnDuration(600, 120, 30, 1000, 1000);
                selfDrivingCar.drive(260, 850, 550, -35, -35);
                driveMotor.hold();

            else:
                selfDrivingCar.driveLine(1800, 1000, 1000, -10, -1);

                for _robotLaps in range (8):
                    hub.imu.reset_heading(0);

                    if (recordListInput[(_robotLaps + 2) % 4][0] == "Parking"):
                        # nParking Loop

                        selfDrivingCar.drive(300, 1000, 1000, -1, -1);
                        selfDrivingCar.streetStall(10, -2, 1000, 1000, 300);
                        selfDrivingCar.street(-500, 0, 750, 650);
                        driveMotor.hold();

                        selfDrivingCar.turn(1, 90, 30, 850, 750);
                        selfDrivingCar.street(500, 90, 900, 850);
                        selfDrivingCar.turn(1, 60, 30, 850, 550);
                        driveMotor.hold();

                        break;

                    else:
                        selfDrivingCar.turn(1, 88, 18, 950, 900);

                        if (recordListInput[(_robotLaps + 2) % 4][2] == "Parking"):
                            # fParking Loop

                            selfDrivingCar.drive(510, 1000, 1000, -10, -5);
                            selfDrivingCar.turnDuration(530, 130, 30, 1000, 1000);
                            selfDrivingCar.turn(1, 90, 30, 850, 550);
                            selfDrivingCar.street(10, 90, 850, 750);
                            selfDrivingCar.drive(100, 850, 550, -35, -35);
                            driveMotor.hold();

                            break;
                            
                        else:
                            selfDrivingCar.driveLine(1800, 1000, 1000, -10, -1);

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    else: # COUNTERCLOCKWISE
        if (recordListInput[1][0] == "Parking"):
            # nParking Start

            selfDrivingCar.street(-600, 0, 750, 650);
            driveMotor.hold();
            selfDrivingCar.turn(1, -88, 30, 850, 750);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, -90, 650, 550);
            driveMotor.hold();

            selfDrivingCar.street(370, -90, 850, 800);
            selfDrivingCar.drive(170, 850, 650, 35, 35);
            driveMotor.hold();

        else:
            selfDrivingCar.street(-320, 0, 750, 650);
            driveMotor.hold();
            selfDrivingCar.turn(1, -88, 30, 850, 750);

            if (recordListInput[1][2] == "Parking"):
                # fParking Start
                driveMotor.hold();
                selfDrivingCar.streetLine(-100, -90, 750, 650);
                driveMotor.hold();
                selfDrivingCar.drive(680, 1000, 1000, 10, 5);
                selfDrivingCar.turnDuration(650, -120, 30, 1000, 1000);
                selfDrivingCar.drive(260, 850, 550, 35, 35);
                driveMotor.hold();

            else:
                selfDrivingCar.driveLine(1800, 1000, 1000, 7, 1);

                for _robotLaps in range (8):
                    hub.imu.reset_heading(0);

                    if (recordListInput[(_robotLaps + 2) % 4][0] == "Parking"):
                        # nParking Loop

                        selfDrivingCar.drive(300, 1000, 1000, 1, 1);
                        selfDrivingCar.streetStall(10, 2, 1000, 1000, 300);
                        selfDrivingCar.street(-600, 0, 750, 650);
                        driveMotor.hold();

                        selfDrivingCar.turn(1, -90, 30, 850, 750);
                        selfDrivingCar.street(500, -90, 900, 850);
                        selfDrivingCar.turn(1, -60, 30, 850, 550);
                        driveMotor.hold();

                        break;

                    else:
                        selfDrivingCar.turn(1, -88, 25, 950, 900);

                        if (recordListInput[(_robotLaps + 2) % 4][2] == "Parking"):
                            # fParking Loop

                            selfDrivingCar.drive(500, 1000, 1000, 10, 5);
                            selfDrivingCar.turnDuration(600, -130, 30, 1000, 1000);
                            selfDrivingCar.turn(1, -90, 30, 850, 550);
                            selfDrivingCar.drive(100, 850, 550, 35, 35);
                            driveMotor.hold();

                            break;
                            
                        else:
                            selfDrivingCar.driveLine(1800, 1000, 1000, 5, 1);

    selfDrivingCar.motorClose();

# recordListMain = [["", "---", "", "---"], ["", "---", "", "---"], ["", "---", "", "---"], ["", "---", "Parking", "---"]];
# _timer = StopWatch();

# obstacleParking(1, recordListMain);
# print(_timer.time());
