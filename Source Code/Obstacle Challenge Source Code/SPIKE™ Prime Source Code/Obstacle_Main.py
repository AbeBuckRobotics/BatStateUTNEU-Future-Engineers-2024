from Obstacle_Start import obstacleStart
from Obstacle_Clockwise import obstacleClockwise
from Obstacle_Counter import obstacleCounter
from Obstacle_UTurn import obstacleUTurn
from Obstacle_Parking import obstacleParking
from pybricks.tools import wait, StopWatch

_clock = StopWatch()
_robotLapsTarget, _robotLaps, _recordListMain = 12, 0, [[None for y in range(4)] for x in range(4)]

_clock.reset()
_robotDirection = obstacleStart()
_timeStart = _clock.time()
_clock.reset()

while (_robotLaps < _robotLapsTarget - 4):
    _robotLaps += 1
    print(f"Laps: {_robotLaps / 4}")

    _recordListMain[_robotLaps % 4] = obstacleClockwise(_recordListMain[_robotLaps % 4], _robotLaps) if (_robotDirection == 1) else obstacleCounter(_recordListMain[_robotLaps % 4], _robotLaps)

_robotUTurn, _recordListMain = obstacleUTurn(_robotDirection, _recordListMain)

if (_robotUTurn == True):
    _robotDirection *= -1
    _robotLaps -= 1

while (_robotLaps < _robotLapsTarget):
    _robotLaps += 1
    print(f"Laps: {_robotLaps / 4}")

    if (_robotDirection == 1):
        obstacleClockwise(_recordListMain[_robotLaps % 4], _robotLaps, _robotLapsTarget)
    else:
        obstacleCounter(_recordListMain[_robotLaps % 4], _robotLaps, _robotLapsTarget)

_timeLoop = _clock.time()
_clock.reset()

obstacleParking(_robotDirection, _recordListMain)
_timeParking = _clock.time()

print(f"\n\nStart: {_timeStart}\tLoop: {_timeLoop}\tParking: {_timeParking}")
print(f"\nScoring Time: {_timeStart + _timeLoop}")
print(f"Round Time: {_timeStart + _timeLoop + _timeParking}")
