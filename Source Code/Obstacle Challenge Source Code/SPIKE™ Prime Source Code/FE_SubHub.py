from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Axis, Button, Color, Direction, Icon, Port, Side, Stop
from pybricks.tools import StopWatch, wait

hub = PrimeHub()
hub.system.set_stop_button([Button.BLUETOOTH])
hub.speaker.volume(100)

leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [1], False, 5)
rightMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5)
colorSensor = ColorSensor(Port.C)

leftMotor.control.limits(2000, 20000, 1000)
rightMotor.control.limits(2000, 20000, 1000)

wait(100)

hold = []

display = [[0, 0, 0, 0, 0], [0, 100, 100, 100, 0], [0, 100, 100, 100, 0], [0, 100, 100, 100, 0], [0, 0, 0, 0, 0]]
hub.display.icon(display)
hub.light.off()

while (len(hub.buttons.pressed()) >= len(hold) and colorSensor.reflection() > 5):
    if (len(hub.buttons.pressed()) > len(hold)):
        hold = hub.buttons.pressed()

leftMotor.reset_angle(0)
rightMotor.reset_angle(0)
colorSensor.lights.on(0)

try:
    while True:
        leftMotor.run_target(1000, 190, Stop.HOLD, False)
        rightMotor.run_target(1000, 190, Stop.HOLD, False)

        hold = hub.buttons.pressed()

        if (Button.CENTER in hold):
            hub.speaker.beep(500)

            ctr = 0
            ifbreak = False
            print(hub.battery.voltage())

            for i in range(1, 4):
                for j in range(1, 4):
                    if (hub.battery.voltage() < 8300 - ctr):
                        hub.display.pixel(i, j, 0)
                    else:
                        ifbreak = True
                        break
                    ctr += 100
                if (ifbreak):
                    break

            while (Button.CENTER in hub.buttons.pressed()):
                pass

finally:
    leftMotor.reset_angle(180)
    rightMotor.reset_angle(180)
    wait(200)
    leftMotor.run_target(500, 0, Stop.HOLD, False)
    rightMotor.run_target(500, 0, Stop.HOLD, False)
    wait(500)
