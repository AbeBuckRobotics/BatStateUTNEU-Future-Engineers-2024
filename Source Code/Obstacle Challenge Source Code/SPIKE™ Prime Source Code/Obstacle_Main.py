# from FE_Start import *
from Obstacle_Start import obstacleStart;
from Obstacle_LoopClockwise import obstacleLoopClockwise;
from Obstacle_LoopCounter import obstacleLoopCounter;
from Obstacle_Parking import obstacleParking;
from pybricks.tools import wait, StopWatch;

# try:
print("\n\n\n");
_timer = StopWatch();
multipleProgramsMenuNumber = 0;

if (multipleProgramsMenuNumber == 0):
    _robotLaps, _timeStraightList, _recordListMain = 0, [], [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]];

    _timer.reset();
    _robotDirection = obstacleStart();
    # _robotDirection = 1;
    _timeStart = _timer.time();

    while (_robotLaps < 12):
        _robotLaps += 1;
        
        print("\nLaps:  " + str(_robotLaps / 4));

        _timer.reset();
        _recordListMain[_robotLaps % 4] = obstacleLoopClockwise(_recordListMain[_robotLaps % 4]) if (_robotDirection == 1) else obstacleLoopCounter(_recordListMain[_robotLaps % 4]);
        print(_recordListMain);
        _timeStraightList.append(_timer.time());

    _timer.reset();
    obstacleParking(_robotDirection, _recordListMain);
    _timeParking = _timer.time();

# except Exception as error:
#   print("An error occurred:", type(error).__name__, "–", error);

# finally:
#     pass;
#     print("\n" + str(_timeStraightList));
#     _timeStraightListSum = 0;

#     for i in range (len(_timeStraightList)):
#         _timeStraightListSum += _timeStraightList[i];

#     print("Start:", _timeStart, "\tLoop:", _timeStraightListSum, "\tTotal:", (_timeStart + _timeStraightListSum), end = "\t");
#     print("Parking:", _timeParking);