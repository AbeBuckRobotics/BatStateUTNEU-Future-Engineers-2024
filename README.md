
***

# BSU Spartan Team – Philippines
[![](https://img.shields.io/badge/FE-Rulebook-2e52af)](https://wro-association.org/wp-content/uploads/WRO-2024-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
[![](https://img.shields.io/badge/YouTube-▶️%20OPEN_CHALLENGE-df3e3e?logo=youtube)](https://youtu.be/06rUdOECv34?si=MXno1v4bBEbKgmpB)
[![](https://img.shields.io/badge/YouTube-▶️%20OBSTACLE_CHALLENGE-df3e3e?logo=youtube)](https://youtu.be/ykb_tLmTXMM?si=5-LzPXuHlno7lfPP)

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This repository provides the BSU Spartan Team’s self-driving car, developed and programmed by our team from the Philippines for the Future Engineers Category. Here, you’ll find details about the robot’s design, functionality, and features, reflecting our dedication to pushing the boundaries of autonomous technology.</p>

***

## The Team:

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Meet the members of the BSU Spartan Team, each bringing unique skills and dedication to our mission at the World Robot Olympiad Turkiye 2024 International Finals. Together, we have combined our knowledge in engineering, programming, and robotics to create a self-driving robot for the Future Engineers category. Driven by a passion for technology and a commitment to excellence, we represent the spirit of teamwork and the pursuit of knowledge</p>

- Joseph Bernard A. Maala, 17, (Right)
- John Angelo M. Bautista, 17, (Left)
  
<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/0.1.png?">

***

## List of Directories

* [`Discussion Images`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Discussion%20Images) contains all the images that is showcased in this README.md file.
* [`History of Vehicle Design`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/History%20of%20Vehicle%20Design) contains the previous versions of the vehicle
* [`List of Materials`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/List%20of%20Materials) contains the list of all the materials necessary to build the robot.
* [`Source Code`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Source%20Code) contains the main and other programs of the robot.
* [`Team Photos`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Team%20Photos) contains multiple photos of the whole team.
* [`Vehicle Building Instructions`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Vehicle%20Building%20Instructions) contains the step by step instructions to contruct the robot.
* [`Vehicle Photos`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Vehicle%20Photos) contains multiple photos of the vehicle.
* [`Vehicle Virtual Model`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Vehicle%20Virtual%20Model) contains multiple images of the vehicle's virtual model.
* [`Video Performance`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Video%20Performance) contains 2 video links showcasing each challenge round.
* [`Wiring Diagram`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Wiring%20Diagram) contains the wiring diagrams of the whole robot including all of its components.

## Main Content

* [Introduction](#introduction)
* [Robot Specifications](#robot-specifications)
* [1. Mobility Management](#1-mobility-management)
  * [1.1. Motor Selection](#11-motor-selection)
  * [1.2. Robot Driving Mechanism](#12-robot-driving-mechanism)
  * [1.3. Robot Design](#13-robot-design)
* [2. Power and Sense Management](#2-power-and-sense-management)
  * [2.1. Power Management](#21-power-management)
    * [2.1.1. SPIKE™ Large Hub](#211-spike-large-hub)
    * [2.1.2 SPIKE™ Large Hub Rechargeable Battery](#212-spike-large-hub-rechargeable-battery)
  * [2.2. Sense Management](#22-sense-management)
    * [2.2.1. SPIKE™ Color Sensor](#221-spike-color-sensor)
    * [2.2.2. SPIKE™ Distance Sensor](#222-spike-distance-sensor)
    * [2.2.3. SPIKE™ Gyro Sensor](#223-spike-gyro-sensor)
    * [2.2.4. OpenMV Cam H7 Plus](#224-openmv-cam-h7-plus)
    * [2.2.5. Additional Information](#225-additional-information)
* [3. Obstacle Management](#3-obstacle-management)
  * [3.1. Open Challenge Strategy](#31-open-challenge-strategy)
    * [3.1.1. Determine Driving Direction](#311-determine-driving-direction)
    * [3.1.2. Wall Avoidance](#312-wall-avoidance)
  * [3.2. Obstacle Challenge Strategy](#32-obstacle-challenge-strategy)
    * [3.2.1. Traffic Sign Detection](#321-traffic-sign-detection)
    * [3.2.2. Parking Lot Detection](#322-parking-lot-detection)
    * [3.2.3. Traffic Sign Avoidance Strategy](#323-traffic-sign-avoidance-strategy)
    * [3.2.4. Parking Lot Strategy](#324-parking-lot-strategy)
    * [3.2.5. Third Lap Continuation](#325-third-lap-continuation)
* [4. Engineering Factor](#4-engineering-factor)
  * [4.1. Rotating Camera & Distance Sensor](#41-rotating-camera--distance-sensor)
  * [4.2. Side Free Wheels](#42-side-free-wheels)
  * [4.3. Camera LEGO Chassis](#43-camera-lego-chassis)
* [5. Recommendations](#5-recommendations)
  * [5.1. Mobility Management Recommendations](#51-mobility-management-recommendations)
  * [5.2. Power and Sense Management Rcommendations](#52-power-and-sense-management-recommendations)
  * [5.3. Obstacle Management Recommendations](#53-obstacle-management-recommendations)
* [6. Construction Guide](#6-construction-guide)
  * [6.1. Robot Construction Guide](#61-robot-construction-guide)
  * [6.2. Program Construction Guide](#62-program-construction-guide)
  * [6.3. Final Step](#63-final-step)

***

## Introduction

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This engineering documentation provides an overview of the BSU Spartan Team's self-driving car, designed for the WRO Turkiye 2024 International Finals. It covers Mobility Management, detailing motor selection, chassis design, and assembly based on principles of speed, torque, and power; Power and Sense Management, explaining the vehicle’s power sources and sensor configurations with a wiring diagram and BOM; and Obstacle Management, outlining strategies for navigating the course with flow diagrams and detailed code. Visual documentation includes images of the robot from all sides and team photos, while performance videos showcase the robot’s functionality across challenges. </p>

***

## Robot Specifications

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The BSU Spartan Team presents this self-driving robot for the World Robot Olympiad Turkiye 2024 International Finals. Designed with precision, agility, and performance in mind, this robot embodies innovation and teamwork by our duo. Engineered to meet the demands of the competition, the Spartan robot features a compact design built with LEGO® and OpenMV Cam H7 Plus, offering optimal speed, maneuverability, and power efficiency. Below are the specifications that highlight the robot’s capabilities, reflecting our team's commitment to excellence and readiness to compete on the global stage.</p>

- **Dimensions**: 195mm (L) x 160mm (W) x 230mm (H)
- **Weight**: 1.23kg
- **Maximum Speed**: 6.53m/s
- **Maximum Steer**: ±60°
- **Steering Torque**: 100Ncm
- **Working Voltage**: 8.3V–7.6V
- **Drive System**: Rear-wheel drive (RWD)
- **Steering Geometry**: Parallel steering
- **Material**: LEGO® Technic

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/0.2.png?">

***

# 1. Mobility Management

### 1.1. Motor Selection

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Motor selection is a crucial part of building the robot since its maneuverability highly depends on it. LEGO® Education SPIKE™ Prime Set has two (2) available motors: SPIKE™ Medium Angular Motor and SPIKE™ Large Angular Motor, which will be referenced as SPIKE™ Medium Motor and SPIKE™ Large Motor respectively. These motors have a lot in common performance-wise and only differ in speed and torque. Based on tests performed with a provision of 7.2V power supply, here are the results: </p>
<br/>

    SPIKE™ Medium Motor                SPIKE™ Large Motor              
      Speed: 135 RPM to 185 RPM          Speed: 135 RPM to 175 RPM
      Torque: 3.5 Ncm to 18 Ncm          Torque: 8 Ncm to 25 Ncm

<sub> RPM – rotations per minute, Ncm – newton centimeter </sub>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Medium Motor was shown to be negligibly faster than the SPIKE™ Large Motor. However, the SPIKE™ Large Motor was able to provide a substantial amount of power compared to its counterpart. With these pieces of information, the team had chosen to use SPIKE™ Large Motors for both driving and steering management, using two (2) SPIKE™ Large Motors in total for the mobility of the robot. </p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Large Motor features an integrated rotation sensor that measures speed, relative position (in degrees), and absolute position (from -180° to +180°) while also detecting manual input when rotated by hand. With a 7.2V power supply, it can achieve a maximum torque of 25 Ncm at stall and a peak efficiency torque of 8 Ncm at 135 RPM, with a no-load speed of 175 RPM. The motor's performance specifications include a sensor resolution of 360 counts per revolution, an accuracy of ±3°, and a 100 Hz update rate for real-time data feedback. Physically, the motor features Technic-compatible build geometry, a 250 mm LEGO® Power Functions 2.0 (LPF2) connector, and dual crosshole outputs for robust integration. </p>

### 1.2. Robot Driving Mechanism

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot uses a parallel steering geometry; a front SPIKE™ Large Motor steers the front wheels of the robot parallel to each other. Meanwhile, the robot is propelled by a rear-wheel drive (RWD) transmission , where power from the rear SPIKE™ Large Motor drives the rear wheels, propelling the robot forward or backward. This steering geometry and transmission setup was chosen by the team because it is commonly used in the Future Engineers Category. Additionally, the team experimented and concluded that the RWD system offered better handling of the robot compared to the front-wheel drive (FWD).</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/1.2.1.png?">

### 1.3. Robot Design

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The electrical components of the robot are mounted on a robot chassis made from LEGO® Technic. These materials were mostly from LEGO® Education SPIKE™ Prime Set and LEGO® Education SPIKE™ Prime Expansion Set, though a few lego parts came from LEGO® MINDSTORMS® Education EV3 Core Set and LEGO® MINDSTORMS® Education EV3 Expansion Set. Additionally, the robot is built to be small so that it can completely fit within the parking lot boundaries while being perpendicular to the wall.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/1.3.1.png?">

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the wheels of the robot, SPIKE™ Large Wheels are incorporated for the rear driving mechanism while EV3 Small Wheels are used for the steering mechanism of the robot. These wheels have a diameter of 88 mm and 43.2 mm respectively. The team decided to use large wheels for the robot's driving base since larger wheels have a higher circumference value compared to the small ones, thus covering longer distances per rotation and increasing the maximum speed limit of the robot. As for steering, large wheels cannot be used since they will block the distance sensor. EV3 Small Wheels showcased the best performance as steering wheels of the robot compared to SPIKE™ Large Wheels, probably due to their smaller size and tire thickness.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/1.3.2.png?">

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As for the weight distribution of the robot, the weight is focused on the rear side of the robot since this is where the driven wheels of the robot are. This is done through the placement of the robot's microcontrollers on the rear side of the robot. This weight distribution should enhance the traction of the said wheels, preventing them from slipping. </p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/1.3.3.png?">

***

# 2. Power and Sense Management

## 2.1. Power Management

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the field of robotics, power management serves as the cornerstone that ensures the operation of an autonomous system. It serves as the brain and heart of the robot. Not only does it play a role in supplying data and energy to the various components, but it also plays a role in optimizing the overall performance of the robot. Below are the figures and details about the components of the robot in the power management section:</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/2.1.0.1.png?">

### 2.1.1. SPIKE™ Large Hub

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Large Hub serves as the primary controller of the robot, controlling most of the components of the robot including its motors and sensors. It is where the robot's main program is downloaded; integrated with MicroPython as the operating system. The hub features six LPF2 input/output ports and a built-in six-axis gyro sensor, which includes a three-axis accelerometer and three-axis gyroscope. Additionally, it has a built-in speaker with a maximum sound quality of 12-bit 16 KHz and can connect to devices via Bluetooth or USB Cable. The team selected this hub as the primary controller for the robot due to its comprehensive capabilities and easy-to-use interface.</p>

### 2.1.2 SPIKE™ Large Hub Rechargeable Battery

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Large Hub Rechargeable Battery is a lithium-ion polymer battery designed to power the SPIKE™ Large Hub, which in turn powers all SPIKE™ motors and sensors. It can be charged inside the Hub using a micro-USB cable and can be removed easily. With a capacity of 2100 mAh and an output of 7.3V, this battery has a lifetime of over 500 cycles, meaning it can handle more than 500 charge-discharge cycles throughout its lifespan.</p>

## 2.2. Sense Management

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Self-driving cars are highly dependent on their sensors in order to drive autonomously. That is why the robot consists of different sensors to properly execute its movements with regards to its position on the game field and obstacles surrounding it. Here are the components of the robot related to its sense management:</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/2.2.0.1.png?">

### 2.2.1. SPIKE™ Color Sensor 

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Color Sensor has the capacity to measure color RGB/HSV, reflection intensity, and ambient intensity. It has a sample rate of 100 Hz and an optimal reading distance of 16 mm. It has three (3) LEDs that can be turned on and off individually at different power levels, making it a possible light output. The team selected this color sensor due to its excellent performance in color detection, far better than the other color sensors the team have.</p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This color sensor is positioned on the front of the robot where it is facing downwards the game field. It is primarily used to read the colored lines on the game field, thus determining the driving direction of the robot. If it has detected the orange line first, the robot would know that the driving direction is clockwise, else if the first detected line was blue, the driving direction is counterclockwise. Additionally, the robot is able to know its position on some parts of the game field that have a clear line to be read by the color sensor.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/2.2.1.1.png?">

### 2.2.2. SPIKE™ Distance Sensor

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The SPIKE™ Distance Sensor has the ability to measure the distance to a surface in front of it with the use of ultrasonic technology. It has a sample rate of 100 Hz and a distance sensing range of 5 cm to 200 cm +/- 2 cm. It has an entrance angle of +/- 35° and has four (4) LEDs that can be turned on and off individually at different power levels, making it a possible light output. It sends inaudible high frequency sound waves from one “eye” while the other “eye” will measure how long it takes the sound waves to reflect through it.</p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This distance sensor is placed on the front of the robot, which is used to determine the position of the robot in respect to the wall in front of the sensor. This allows the robot to navigate safely within the game field, continuously checking if the robot is near the outer boundary wall in Open Challenge Rounds since the robot may not touch the said wall. In addition to that, it is also used to identify the position of the parking lot in Obstacle Challenge Rounds.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/2.2.2.1.png?">

### 2.2.3. SPIKE™ Gyro Sensor

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The built-in SPIKE™ Gyro Sensor can keep track of the angle the hub is currently facing. It consists of a three-axis accelerometer and three-axis gyroscope. The gyroscope part records the change of rotation of the hub and measures the total angle of rotation in degrees, enabling it to return the hub's exact rotation angle around a given axis. Combined with the accelerometer, it allows the hub to determine its orientation and acceleration along a given axis. </p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot relies on this gyro sensor for most of its movements, facilitating its accurate navigation across the whole game field. It enables the robot to follow a specific angle when moving, thus making it drive straight and turn into a particular angle efficiently.</p>

### 2.2.4. OpenMV Cam H7 Plus

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The OpenMV Cam H7 Plus is a compact, low-power microcontroller board that functions as an interactive camera, making it easy to implement- real-world applications using machine vision. This camera is programmable using high-level Python scripts(powered by the MicroPython operating system). This makes it easier to deal with the complex outputs of machine vision algorithms and working with high level data structures. </p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The OpenMV Cam H7 Plus is equipped with an STM32H743II ARM Cortex M7 processor running at 480 MHz with 32MBs SDRAM + 1MB of SRAM and 32 MB of external flash + 2 MB of internal flash. All I/O pins output 3.3V and are 5V tolerant. Additionally, it includes a full speed USB interface to connect directly to your computer. Moreover, the camera is fitted with a 2.8 mm lens on a standard M12 lens mount and uses an 0V5640 image sensor that is capable of capturing images at resolution of 2592x1944 equivalent to 5MP images. It can run the machine vision algorithms between 25-50 FPS on 320x420 resolutions and below. </p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The team selected the OpenMV Cam H7 Plus to specifically detect traffic signs and their colors during the Obstacle Challenge Rounds. This enables the robot to navigate accordingly,  keeping itself to the right side of the track when a red traffic sign obstacle is detected and to the left side of the track when a green traffic sign obstacle is detected. The camera provides a more accurate detection by analyzing pixel density, which helps identify objects based on the density of color pixels detected. A higher pixel density of the closest object indicates what color it is, allowing the robot to process this information and send it through the central hub and execute the appropriate action to avoid the obstacle. </p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/2.2.4.1.png?">

### 2.2.5. Additional Information

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both the SPIKE™ Distance Sensor and OpenMV Cam H7 Plus are mounted to a SPIKE™ Large Motor. For more information, visit [<i>4.1. Rotating Camera & Distance Sensor</i>](#41-rotating-camera--distance-sensor) in [<i>Chapter 4: Engineering Factor</i>](#4-engineering-factor).</p>

***

# 3. Obstacle Management

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In order to detect and negotiate with the present obstacles on the field, a specific strategy must be well-planned to possibly complete three (3) laps in both Open and Obstacle Challenge Rounds. The team had spent a fair amount of time considering different thoughts and ideas to efficiently manage these obstacles; always giving space for new yet excellent ideas to be added in the team's strategy.</p>

## 3.1. Open Challenge Strategy

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Open Challenge Rounds, the only obstacles present on the game field are its outer boundary wall and the randomly placed inner wall. The robot must not touch the outer wall and must not move the inner wall to successfully finish the three laps requirement.</p>

### 3.1.1. Determine Driving Direction

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To determine if the driving direction is clockwise or counterclockwise, the SPIKE™ Color Sensor is used. This sensor is programmed to record the color of the line the robot will first pass: if it is orange, the driving direction is clockwise; if it is blue, the driving direction is counterclockwise.</p>

```py
# (pseudocode) robot determining the driving direction based on the line color

if (lineColor == "Orange"):
    robotDirection = "Clockwise"
elif (lineColor == "Blue"):
    robotDirection == "Counterclockwise"
```

### 3.1.2. Wall Avoidance

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To successfully avoid touching the outer boundary wall, the robot is programmed to perform a 90° turn when it is within a specific distance from the wall. This ensures that the robot will not be near the outer wall after completing each turn. The SPIKE™ Distance Sensor is used to detect if the robot is about to collide with the outer wall. If a collision is about to occur, the robot is programmed to steer away from the wall. Additionally, the SPIKE™ Gyro Sensor is used which allows the robot to follow a specific angle, ensuring that the robot turns properly and drives straight after each turn.</p>

```py
# (pseudocode) robot moving away from the outer wall when it is about to touch the said wall

if (robot.nearOuterWall()):
    robot.moveAway()
```

## 3.2. Obstacle Challenge Strategy

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Obstacle Challenge Rounds, the number of obstacles on the game field increases significantly. In addition to the outer boundary wall and the randomly placed inner wall, there are up to seven (7) traffic signs and two (2) parking lot boundaries, all which are randomly positioned on the game field. The traffic signs are also random in color; they may be green or red. The robot must pass a green traffic sign to the left and a red traffic sign to the right, and the robot must park between the parking lot boundaries after finishing three laps. Lastly, the robot must not touch any of the traffic signs and parking lot boundaries.</p>

### 3.2.1. Traffic Sign Detection

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The camera is programmed to use LAB thresholds to identify the color of the traffic signs, which should be either green or red. A proper given threshold can be obtained with different ways, but trial and error should be enough and being familiarized with the LAB color space could help. Here are the LAB thresholds of the team for the obstacles:</p>

```py
_GREEN = const((0, 100, -128, -10, 20, 127))
_RED = const((0, 100, 7, 127, -10, 127))
# format: (Lmin, Lmax, Amin, Amax, Bmin, Bmax)
```
    
<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The pixels from the image that is read by the camera turn white if they are within the range of the given LAB threshold, else they turn black. The `find_blobs()` function of the `image` module is used to detect these converted pixels. </p>

```py
gBlobs = img.find_blobs([_GREEN], roi = [0, 0, 320, 240], pixels_threshold = 150)
rBlobs = img.find_blobs([_RED], roi = [80, 0, 160, 240], pixels_threshold = 250)
# roi = region of interest; pixels_threshold = minimum pixel count
```

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/3.1.1.png?">

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The necessary data from each colored traffic signs is saved, including the x and y coordinates of their centroid as well as their pixel number. These values are saved to determine the relative position of the traffic signs in respect to the position of the robot.</p>

```py
gPix = g.pixels()
gCx = gBlob.cx()
gCy = gBlob.cy()

rPix = r.pixels()
rCx = rBlob.cx()
rCy = rBlob.cy()
```

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The necessary data from the camera must be transferred to the main hub in order to determine what does the robot need to do. This is done with the use of external libraries [`pupremote.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/pupremote.py) and [`lpf2.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/lpf2.py); these two (2) are used to send the data from the camera. Another external library, [`pupremote_hub.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/SPIKE%E2%84%A2%20Prime%20Source%20Code/pupremote_hub.py), is used for the main hub to receive the data. These external libraries are made by AntonsMindstorms.</p>

```py
# send data from OpenMV Cam H7 Plus to SPIKE™ Large Hub

from pupremote import PUPRemoteSensor, OPENMV

camera = PUPRemoteSensor(power = True)
camera.add_channel('blob', to_hub_fmt = 'hhhhhh')

camera.update_channel('blob', gCx, gCy, gPix, rCx, rCy, rPix)
camera.process()

```

```py
# receive data from OpenMV Cam H7 Plus to SPIKE™ Large Hub

from pupremote_hub import PUPRemoteHub

camera = PUPRemoteHub(Port.E)
camera.add_command('blob', 'hhhhhh')

gtsCall = camera.call('blob')
```

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The main program for traffic sign detection is provided here: [`FE_ObstacleRecognition.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/FE_ObstacleRecognition.py). This program is uploaded to the OpenMV Cam H7 Plus. For the step by step guide how the program is compiled and uploaded to the camera, refer to [<i>Camera Program Guide</i>](#camera-program-guide) in [<i>Chapter 6: Construction Guide</i>](#6-construction-guide)</p>

### 3.2.2. Parking Lot Detection

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In order to determine if there is a presence of parking lot in each straightforward section, the distance sensor of the robot is used instead of the camera. The team have selected this approach since it doesn't require them to find the proper LAB threshold for the color of the parking lot. The `distance()` function of the `pupdevices` module is used to determine if there is a presence of the parking lot.</p>

```py
print(distanceSensor.distance(), end = " ")

if (distanceSensor.distance() < gpDistanceTarget):
    return "Parking"
else:
    return "Normal"
```

### 3.2.3. Traffic Sign Avoidance Strategy

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The whole program for the robot involves single-instance detection of the obstacles instead of the commonly used continuous detection for this category. This means that the robot is programmed to capture the data from the camera only at specific intervals. The team have selected this approach because it is easier for them to debug in the official competition.</p>

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The main strategy for the robot involves programming it to follow three (3) possible routes which are determined based on the color of the traffic signs, the presence of the parking lot, and the defined driving direction of the challenge round. For example, the driving direction is set to Clockwise. If the detected color of the traffic sign is `Green`, the robot will glide itself to the outer wall, successfully passing the traffic sign to its left. If the detected color is `Red`, the robot will glide itself to the inner wall, successfully passing the traffic sign to its right. However, if the detected color is `Green` and there is a detected presence of the parking lot, the robot will go through somewhere between the outer and inner walls. You can refer to the illustration below for better visualization; the arrows represent the route the robot would take for each possibility.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/3.3.1.png?">

* Green arrow – Green traffic sign
* Red arrow – Red traffic sign
* Gray arrow – Green traffic sign with presence of parking lot

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the robot wasn't able to detect the color of the traffic sign, the robot would follow either the `Green` traffic sign or `Red` traffic sign route. If ever the color of the traffic signs in the same straightforward sections are different, which is very likely, the robot will follow the same logic stated earlier. Here is another illustration for better visualization:</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/3.3.2.png?">

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lastly, the robot is programmed to record the color and position of the traffic signs encountered of each straightforward section during its first lap. This approach ensures that there will be no false detections during its second and third lap.</p>

### 3.2.4. Parking Lot Strategy

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Similar to the traffic signs, the robot is set to record the position of the parking lot on the field during its first lap. Having a reference of the position of the parking lot, the robot is programed to follow a specific route: the robot will glide itself to the outer wall until it reaches the corner section before the straightforward section where the parking lot is positioned. The robot will then follow the route for the Green traffic sign with presence of parking lot, which is showcased in Figure 3.4 earlier. Afterwards, the robot will perform a perpendicular parking between the parking lot boundaries, marking the end of the run for the Obstacle Challenge Round. A following illustration is provided for a better visualization.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/3.4.1.png?">

### 3.2.5. Third Lap Continuation

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot must continue to the third lap in the in the opposite direction if the last traffic sign detected is Red. In order to determine if the robot must perform the said action, the robot uses the recorded color and position of traffic signs it detected during the first lap. If ever the last detected traffic sign is Red, the robot would make its turn in the next corner section of the starting straightforward section of the robot. Here is an illustration demonstrating the route the robot will take for the third lap continuation:</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/3.5.1.png?">

* The position of the yellow car is where the robot starts.

***

## 4. Engineering Factor

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The whole physical structure of the robot was completely designed and manufactured by the team out of LEGO® Technic. While there are standard off-the-shelf electrical components such as motors and sensors for the robot's functionality, the robot's design remains unique, embodying innovative features that set it apart from typical robots. Here are such features:</p>

### 4.1. Rotating Camera & Distance Sensor

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In order to maximize the functionality of the camera and distance sensor, the robot is equipped with a SPIKE™ Large Motor that allows these sensors to rotate for approximately 135° in both directions starting from the middle. This rotating capability enables these two (2) sensors to capture a wider view of the robot's surroundings, enhancing the robot's ability to detect and navigate through obstacles and the whole game field. The team developed this feature since the limited ports of the SPIKE™ Large Hub cannot provide room for more sensors around the robot. This motor serves as a helpful tool in the detection of the walls, obstacles, and overall surroundings of the robot while it is in the game field.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/4.0.1.png?">

### 4.2. Side Free Wheels

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot is equipped with medium-size gears on its sides, acting as free wheels, allowing for uninterrupted movements when it is about to encounter a wall at an angle. Normally, the robot will be stuck or interrupted when a wall is approached diagonally. However, these free wheels enable the robot to glide smoothly along the surface of the wall, perfectly aligning itself to the wall. This design minimizes the possible disruptions in movement and enables the robot to adjust its position precisely. </p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/4.0.2.png?">

### 4.3. Camera LEGO Chassis

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The OpenMV Cam H7 Plus is securely placed inside the custom-designed LEGO camera mount which was uniquely designed by the team. The mount structures integrate LEGO components, making it easy to attach the camera onto the rotating large motors. This LEGO design maintains its uniformity with the overall robot and allows for convenient attachment of additional external components, such as a color sensor placed behind the camera.</p>

<img src = "https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Discussion%20Images/4.0.3.png?">

***

# 5. Recommendations

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot has come a long way since its development, yet there are still areas where it can be refined and optimized. The team first assessed the limitations of the robot to identify possible recommendations that should address these current limitations and anticipate future challenges. These recommendations aim to enhance the overall performance, reliability, and functionality of the robot.</p>

### 5.1. Mobility Management Recommendations

- <p align = "justify">Incorporate a [differential gear](https://en.wikipedia.org/wiki/Differential_(mechanical_device)) into the robot's driving mechanism for smooth and stable turns by letting the wheels rotate at different speeds. This is important since for instance, during a right turn, the left wheel, being farther from the center of the turn, must cover a larger distance along the circular path than the right wheel within the same duration.</p>
- <p align = "justify">Select or develop custom wheels with appropriate dimensions and proper tires for better traction on the game field. This would lessen tire slip, improving the precision of the motor encoders thus enhancing the consistency of the robot.</p>
- <p align = "justify">Try other types of steering geometry, particularly the [Ackerman steering mechanism](https://en.wikipedia.org/wiki/Ackermann_steering_geometry) which allows a car to turn while avoiding tire slip. Though it is not that easy to implement, it should allow smoother and sharper turns if incorporated correctly, allowing the robot for a wider range of movements.</p>
- <p align = "justify">Test the capability of [all-wheel drive (AWD) transmission](https://en.wikipedia.org/wiki/All-wheel_drive_vehicle) which may improve the speed, acceleration, and stability of the robot. This is due to the fact that it distributes power across all four wheels, reducing the chance of wheels losing traction at high acceleration. However, it should be taken into consideration that AWD systems typically consume more weight than RWD, which can reduce the maximum speed of the robot. </p>

### 5.2. Power and Sense Management Recommendations

- <p align = "justify">Switch to other microcontrollers such as [Arduino Uno](https://docs.arduino.cc/hardware/uno-rev3/) or [Raspberry Pi](https://www.raspberrypi.com/). These microcontrollers are able to handle more motors and sensors, and control a wide variety of electrical components, in comparison to the team's current SPIKE™ Large Hub, it can only control a maximum of six (6) selected motors and sensors. Therefore it is better if there is an additional port that can attach an additional motor for driving to maximize the speed of the robot and more sensors can be attached to make the robot more reliable.</p>
- <p align = "justify">Explore a better suited camera like [Raspberry Pi Camera Module 2](https://www.raspberrypi.com/products/camera-module-v2/) or [NVIDIA Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/) that has a better processing power and memory capacity, making them more capable of memory-intensive algorithms. These cameras can handle complex machine learning models and offer a higher image quality.</p>
- <p align = "justify">Swap to much more advanced sensors that can return accurate and precise values in a short given amount of time while still consuming a reasonable amount of power. The team wasn't able to maximize the functionality of the robot's distance sensor because of its inaccuracy, hindering the robot from  consistently reading the position of the parking lot boundaries.</p>

### 5.3. Obstacle Management Recommendations

- <p align = "justify">Consider an obstacle challenge strategy with continuous detection of the traffic signs rather than a single-instance detection which causes a lot of movements. In addition to that, try to apply various detection methods beyond simple pixel-based such as object tracking, which is the recognition and tracking of items along through an image processing application. This offers the advantage of consistently following a target unlike simple pixel-based methods.

***

# 6. Construction Guide

## 6.1. Robot Construction Guide

1. <p align = "justify">Prepare these necessary robotics sets and camera for the build of the robot. You may refer to the [<i>Bills of Materials</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/List%20of%20Materials/Bills_of_Materials.png) for the amount and total cost:</p>
    - [LEGO® Education SPIKE™ Prime Set](https://education.lego.com/en-us/products/lego-education-spike-prime-set/45678/)
    - [LEGO® Education SPIKE™ Prime Expansion Set](https://education.lego.com/en-us/products/lego-education-spike-prime-expansion-set/45681/)
    - [LEGO® MINDSTORMS® Education EV3 Core Set](https://education.lego.com/en-us/products/lego-mindstorms-education-ev3-core-set/5003400/)
    - [LEGO® MINDSTORMS® Education EV3 Expansion Set](https://sasbadilearning.com/product/mindstorms-education-ev3-expansion-set/)
    - [OpenMV Cam H7 Plus](https://openmv.io/products/openmv-cam-h7-plus)
  
2. <p align = "justify">Prepare the specific parts that will be included in the robot. You may refer to the [<i>Table of Materials</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/List%20of%20Materials/Table%20of%20Materials) for the exact quantity of parts that the robot will consist.</p>
  
3. <p align = "justify">Build the robot. You may refer to the [<i>Building Instructions</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Vehicle%20Building%20Instructions) of the team's robot to have a starting idea.</p>

4. <p align = "justify">Finally, ensure that every electrical components are wired properly according to the [<i>Pictorial Diagram</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Wiring%20Diagram/Robot%20Pictorial%20Diagram.png?) of the team's robot.</p>

## 6.2. Program Construction Guide

### Camera Program Guide

1. <p align = "justify">Prepare [OpenMV IDE](https://openmv.io/pages/download) which is necessary for the compilation of the program to the robot's camera.</p>

2. <p align = "justify">You will need these external libraries made by AntonsMindstorms: [`pupremote.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/pupremote.py) and [`lpf2.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/lpf2.py). This library allows the robot's camera to transfer its data to the robot's microcontroller.</p>

3. <p align = "justify">To begin programming, you are first recommended to read the [OpenMV Cam Documentation](https://docs.openmv.io/index.html) to understand how the functions and the whole codebase works. OpenMV IDE has a default starting program which you can freely edit. The team have provided their program which can be found here: [`FE_ObstacleRecognition.py`](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/blob/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code/FE_ObstacleRecognition.py). </p>

4. <p align = "justify">Connect the camera to the computer with a use of an USB cable. The camera's LED should blink green multiple times and white once, indicating that the camera has been successfully detected by the computer. With the OpenMV IDE, click the `Connect` button on the bottom-left or press `Ctrl+E` to connect the camera to the application. The `Run Script` button below should turn green, indicating that the camera is successfully connected to the OpenMV IDE. </p>

5. <p align = "justify">To run the program, click the `Run Script` button or press `Ctrl+R`. To stop the program, the same button and keys are used.</p>

6. <p align = "justify">To upload the program to the camera, proceed to the top-left of the OpenMV IDE. Click `Tools` then `Save open script to OpenMV Cam (as main.py)`.</p>

7. <p align = "justify">The whole program of the team for the camera and its necessary libraries are compiled here: [<i>Obstacle Challenge Camera Source Code</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/Camera%20Source%20Code). </p>

### SPIKE™ Prime Program Guide

1. <p align = "justify">Prepare [Pybricks Code](https://code.pybricks.com/) which is necessary for the compilation of the program to the robot's microcontroller.</p>

2. <p align = "justify">You need to first install the Pybricks firmware on your SPIKE™ Large Hub. You may follow the instructions from Pybricks' official website here: [Installing Pybricks On The Hub](https://pybricks.com/learn/getting-started/install-pybricks/#installing-pybricks-on-the-hub).</p>

3. <p align = "justify">To begin programming, you are first recommended to read the [Pybricks Documentation](https://code.pybricks.com/static/docs/v2.19.0/index.html) to understand how the robot can move and sense its surroundings. You may follow the instructions from Pybrick's official website here: [Creating Your First Program](https://pybricks.com/learn/getting-started/pybricks-environment/).</p>
   
5. <p align = "justify">Connect the hub to the computer with Bluetooth. Click the `Bluetooth` icon on the top-right, choose which hub you plan to connect, then click `Pair`. </p>

6. <p align = "justify">To run the program to the hub, click the `Run this program` button or press `F5`. To stop the program, click the `Stop everything` button or press `F6`.</p>

7. <p align = "justify">To upload the program to the hub, Pybricks automatically downloads the program you ran to the hub. This means that whenever you run the program to the hub, it is also saved there at the same time.</p>

8. <p align = "justify">The whole program of the team for the Open Challenge is provided in [<i>Open Challenge Source Code</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Source%20Code/Open%20Challenge%20Source%20Code). For the Obstacle Challenge, it is provided here [<i>Obstacle Challenge SPIKE™ Prime Source Code</i>](https://github.com/AbeBuck/BSU-Spartan-Team_FE-2024/tree/main/Source%20Code/Obstacle%20Challenge%20Source%20Code/SPIKE%E2%84%A2%20Prime%20Source%20Code).</p>

## 6.3. Final Step

<p align = "justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The team strongly encourages everyone to enhance their program and robot build as true engineering involves not only creating solutions but also sharing ideas with others to drive innovation forward. You may refer to the team's [<i>Chapter 5: Recommendations</i>](#5-recommendations) for their insights on how you can improve their work. By building upon each other's work, we can collectively advance the project to new levels, allowing it to evolve and reach its full potential through teamwork.</p>

