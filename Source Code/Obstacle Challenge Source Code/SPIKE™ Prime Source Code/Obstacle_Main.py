from Obstacle_Start import obstacleStart
from Obstacle_Clockwise import obstacleClockwise
from Obstacle_Counter import obstacleCounter
from Obstacle_UTurn import obstacleUTurn
from Obstacle_Parking import obstacleParking
from pybricks.tools import wait, StopWatch

_clock = StopWatch()
_robotLaps, _recordListMain = 0, [[None for y in range(4)] for x in range(4)]

_clock.reset()
_robotDirection = obstacleStart()
_timeStart = _clock.time()

while (_robotLaps < 12):
    _robotLaps += 1

    print(f"Laps: {_robotLaps / 4}")

    _recordListMain[_robotLaps % 4] = obstacleClockwise(_recordListMain[_robotLaps % 4], _robotLaps) if (_robotDirection == 1) else obstacleCounter(_recordListMain[_robotLaps % 4], _robotLaps)
    # _recordListMain = [[None for y in range(4)] for x in range(4)]

obstacleParking(_robotDirection, _recordListMain)

print(f"\nFINAL TIME: {_clock.time()}")
