from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Axis, Button, Color, Direction, Icon, Port, Side, Stop
from pybricks.tools import wait, Matrix, StopWatch
from umath import sin, pi

hub = PrimeHub();
timer = StopWatch();

hub.system.set_stop_button([Button.BLUETOOTH]);
hub.speaker.volume(100);
hub.display.off();
hub.light.off();

def multipleProgramsMenu():
    multipleProgramsMenuNumber = 0;

    while (True):
        multipleProgramsMenuButtonsPressed = hub.buttons.pressed();
        hub.display.off();

        if (multipleProgramsMenuNumber == 20):
            multipleProgramsMenuNumber = 0;
        elif (multipleProgramsMenuNumber == -1):
            multipleProgramsMenuNumber = 19;

        if (multipleProgramsMenuNumber % 10 == 0):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 100, 0, 100, 0], [0, 100, 0, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 1):
            multipleProgramsMenuDisplay = [[0, 0, 100, 0, 0], [0, 0, 100, 0, 0], [0, 0, 100, 0, 0], [0, 0, 100, 0, 0], [0, 0, 100, 0, 0]];
        elif (multipleProgramsMenuNumber % 10 == 2):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 100, 100, 100, 0], [0, 100, 0, 0, 0], [0, 100, 100, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 3):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 100, 100, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 4):
            multipleProgramsMenuDisplay = [[0, 100, 0, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 0, 0, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 5):
            multipleProgramsMenuDisplay = [ [0, 100, 100, 100, 0], [0, 100, 0, 0, 0], [0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 100, 100, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 6):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 100, 0, 0, 0], [0, 100, 100, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0]];
        elif (multipleProgramsMenuNumber % 10 == 7):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 0, 100, 0, 0], [0, 100, 0, 0, 0], [0, 100, 0, 0, 0]];
        elif (multipleProgramsMenuNumber % 10 == 8):
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0]];
        else:
            multipleProgramsMenuDisplay = [[0, 100, 100, 100, 0], [0, 100, 0, 100, 0], [0, 100, 100, 100, 0], [0, 0, 0, 100, 0], [0, 100, 100, 100, 0]];

        if (multipleProgramsMenuNumber // 10 == 1):
            for multipleProgramsMenuLoopStart1 in range (5):
                for multipleProgramsMenuLoopStart2 in range (3):
                    multipleProgramsMenuDisplay[multipleProgramsMenuLoopStart1][-1 - multipleProgramsMenuLoopStart2] = multipleProgramsMenuDisplay[multipleProgramsMenuLoopStart1][-2 - multipleProgramsMenuLoopStart2];

                multipleProgramsMenuDisplay[multipleProgramsMenuLoopStart1][0] = 100;
                multipleProgramsMenuDisplay[multipleProgramsMenuLoopStart1][1] = 0;

        hub.display.icon(multipleProgramsMenuDisplay);

        while not any(multipleProgramsMenuButtonsPressed):
            multipleProgramsMenuButtonsPressed = hub.buttons.pressed();
        while any(hub.buttons.pressed()):
            pass;

        if (Button.LEFT in multipleProgramsMenuButtonsPressed):
            multipleProgramsMenuNumber -= 1;
        elif (Button.RIGHT in multipleProgramsMenuButtonsPressed):
            multipleProgramsMenuNumber += 1;
        elif (Button.CENTER in multipleProgramsMenuButtonsPressed):
            hub.display.off();
            break;

    return multipleProgramsMenuNumber;

def portChecker(portCheckerPort, portCheckerIndex):
    portCheckListPrevious = portCheckList[portCheckerIndex];

    try:
        portCheck = PUPDevice(portCheckerPort);
        portCheckList[portCheckerIndex] = 0;
    except:
        portCheckList[portCheckerIndex] = 100;

    if (portCheckList[portCheckerIndex] != portCheckListPrevious):
        hub.speaker.beep(500);
        return True;
    else:
        return False;

def hubCustomDisplay(hubCustomDisplayHub, hubCustomDisplayIcon):
    hubCustomDisplayBrightness = list(range(0, 100, 10)) + list(range(100, 0, -10))
    hubCustomDisplayHub.display.animate([hubCustomDisplayIcon * i / 100 for i in hubCustomDisplayBrightness], 30);

def hubCustomLight(hubCustomLightHub, hubCustomLightColor):
    hubCustomLightBrightness = list(range(0, 10, 1)) + list(range(10, 0, -1));
    hubCustomLightHub.light.animate([hubCustomLightColor * (0.5 * sin(i / 15 * pi) + 0.5) for i in hubCustomLightBrightness], 40);

portCheckList = [0, 0, 0, 0, 0, 0];

try: 
    groundColorSensor = ColorSensor(Port.A);
except:
    portCheckList[0] = 100;
try: 
    driveMotor = Motor(Port.B, Direction.CLOCKWISE, [1], False, 500);
except:
    portCheckList[1] = 100;
try: 
    distanceSensor = UltrasonicSensor(Port.C);
except:
    portCheckList[2] = 100;
try: 
    steerMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1], False, 5);
except:
    portCheckList[3] = 100;
try: 
    visionMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5);
except:
    portCheckList[4] = 100;
try:
    cameraColorSensor = ColorSensor(Port.F);
except:
    portCheckList[5] = 100;

if (100 not in portCheckList):
    try:
        groundColorSensor.lights.on(0);
        cameraColorSensor.lights.on(0);
        distanceSensor.lights.on(0);
        hub.speaker.volume(100);
        hub.speaker.beep(300);

    finally:
        groundColorSensor.lights.on(0);
        cameraColorSensor.lights.on(0);
        distanceSensor.lights.on(0);

        driveMotor.close();
        steerMotor.close();
        visionMotor.close();

        print("\n\n\n");

else:
    portCheckListPrevious = [];
    portCheckDeterminator = True;

    while True:
        if (portCheckDeterminator):
            if (100 not in portCheckList):
                hubCustomDisplay(hub, Matrix([[100, 100, 100, 100, 100], [100, 70, 70, 70, 100], [100, 70, 50, 70, 100], [100, 70, 70, 70, 100], [100, 100, 100, 100, 100]]));
            else:
                hubCustomDisplay(hub, Matrix([[portCheckList[0], portCheckList[0] - 40 , 0, portCheckList[1] - 30, portCheckList[1]], [0, 0, 0, 0, 0], [portCheckList[2], portCheckList[2] - 40 , 0, portCheckList[3] - 30, portCheckList[3]], [0, 0, 0, 0, 0], [portCheckList[4], portCheckList[4] - 30, 0, portCheckList[5] - 30, portCheckList[5]]]));

            portCheckDeterminator = False;

        portCheckA = portChecker(Port.A, 0);
        portCheckB = portChecker(Port.B, 1);
        portCheckC = portChecker(Port.C, 2);
        portCheckD = portChecker(Port.D, 3);
        portCheckE = portChecker(Port.E, 4);
        portCheckF = portChecker(Port.F, 5);
        
        if (portCheckA or portCheckB or portCheckC or portCheckD or portCheckE or portCheckF):
            portCheckDeterminator = True;
        else:
            portCheckDeterminator = False;