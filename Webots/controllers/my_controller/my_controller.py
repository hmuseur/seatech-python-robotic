"""my_controller controller."""

from controller import Robot, Motor, DistanceSensor, PositionSensor
from typing import Union

class RobotMotor(Motor):
    def __init__(self,name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        print(self.getMaxVelocity())

class RobotMotors():
    def __init__(self,speed=None):
        self.__wheel_motor00 = RobotMotor('wheel_motor00')
        self.__wheel_motor01 = RobotMotor('wheel_motor01')
        self.__wheel_motor02 = RobotMotor('wheel_motor02')
        self.__wheel_motor03 = RobotMotor('wheel_motor03')
        self.__wheel_motor04 = RobotMotor('wheel_motor04')
        self.__wheel_motor05 = RobotMotor('wheel_motor05')
        self.__wheel_motor06 = RobotMotor('wheel_motor06')
        self.__wheel_motor07 = RobotMotor('wheel_motor07')
        self.__wheel_motor08 = RobotMotor('wheel_motor08')
        self.__wheel_motor09 = RobotMotor('wheel_motor09')

    def go_front(self):
        self.__wheel_motor00.setVelocity(15)
        self.__wheel_motor01.setVelocity(15)
        self.__wheel_motor02.setVelocity(15)
        self.__wheel_motor03.setVelocity(15)
        self.__wheel_motor04.setVelocity(15)
        self.__wheel_motor05.setVelocity(15)
        self.__wheel_motor06.setVelocity(15)
        self.__wheel_motor07.setVelocity(15)
        self.__wheel_motor08.setVelocity(15)
        self.__wheel_motor09.setVelocity(15)
    
    def go_back(self):
        self.__wheel_motor00.setVelocity(-15)
        self.__wheel_motor08.setVelocity(-15)
        self.__wheel_motor01.setVelocity(-15)
        self.__wheel_motor02.setVelocity(-15)
        self.__wheel_motor03.setVelocity(-15)
        self.__wheel_motor04.setVelocity(-15)
        self.__wheel_motor05.setVelocity(-15)
        self.__wheel_motor06.setVelocity(-15)
        self.__wheel_motor07.setVelocity(-15)
        self.__wheel_motor08.setVelocity(-15)
        self.__wheel_motor09.setVelocity(-15)

    def go_turnright(self):
        self.__wheel_motor00.setVelocity(15)
        self.__wheel_motor01.setVelocity(15)
        self.__wheel_motor02.setVelocity(15)
        self.__wheel_motor03.setVelocity(15)
        self.__wheel_motor04.setVelocity(15)
        self.__wheel_motor05.setVelocity(-15)
        self.__wheel_motor06.setVelocity(-15)
        self.__wheel_motor07.setVelocity(-15)
        self.__wheel_motor08.setVelocity(-15)
        self.__wheel_motor09.setVelocity(-15)

    def go_turnleft(self):
        self.__wheel_motor00.setVelocity(-15)
        self.__wheel_motor01.setVelocity(-15)
        self.__wheel_motor02.setVelocity(-15)
        self.__wheel_motor03.setVelocity(-15)
        self.__wheel_motor04.setVelocity(-15)
        self.__wheel_motor05.setVelocity(15)
        self.__wheel_motor06.setVelocity(15)
        self.__wheel_motor07.setVelocity(15)
        self.__wheel_motor08.setVelocity(15)
        self.__wheel_motor09.setVelocity(15)

class Distance():
    def __init__(self):
        self.__ds0_distance_sensor = DistanceSensor('ds0')
        self.__ds1_distance_sensor = DistanceSensor('ds1')
        self.__ds2_distance_sensor = DistanceSensor('ds2')
        self.__ds3_distance_sensor = DistanceSensor('ds3')

    
    def getDistanceValue(self):
        return [self.__ds0_distance_sensor.getValue(),
        self.__ds1_distance_sensor.getValue(),
        self.__ds2_distance_sensor.getValue(),
        self.__ds3_distance_sensor.getValue()]

class Position():
    def __init__(self):
        self.__wheel_sensor00_position_sensor = PositionSensor('wheel_sensor00')
        self.__wheel_sensor01_position_sensor = PositionSensor('wheel_sensor01')
        self.__wheel_sensor02_position_sensor = PositionSensor('wheel_sensor02')
        self.__wheel_sensor03_position_sensor = PositionSensor('wheel_sensor03')
        self.__wheel_sensor04_position_sensor = PositionSensor('wheel_sensor04')
        self.__wheel_sensor05_position_sensor = PositionSensor('wheel_sensor05')
        self.__wheel_sensor06_position_sensor = PositionSensor('wheel_sensor06')
        self.__wheel_sensor07_position_sensor = PositionSensor('wheel_sensor07')
        self.__wheel_sensor08_position_sensor = PositionSensor('wheel_sensor08')
        self.__wheel_sensor09_position_sensor = PositionSensor('wheel_sensor09')

    
    def getPositionValue(self):
        return [self.__wheel_sensor00_position_sensor.getValue(),
        self.__wheel_sensor01_position_sensor.getValue(),
        self.__wheel_sensor02_position_sensor.getValue(),
        self.__wheel_sensor03_position_sensor.getValue(),
        self.__wheel_sensor04_position_sensor.getValue(),
        self.__wheel_sensor05_position_sensor.getValue(),
        self.__wheel_sensor06_position_sensor.getValue(),
        self.__wheel_sensor07_position_sensor.getValue(),
        self.__wheel_sensor08_position_sensor.getValue(),
        self.__wheel_sensor09_position_sensor.getValue()]


class Robotfighter(Robot):
    def __init__(self):
        super().__init__()
        self.motors=RobotMotors()
        self.distances=Distance()
        self.positions=Position()

    # def go(self):
    #     self.motors.go_back()

    # def go_front(self):
    #     self.motors.go_front()
    
    # def go_turnright(self):
    #     self.motors.go_turnright()
    
    # def go_turnleft(self):
    #     self.motors.go_turnleft()
    
    def run(self, direction):
        if direction=="F":
            self.motors.go_front()
        elif direction=="B":
            self.motors.go_back()
        elif direction=="R":
            self.motors.turn_right()
        elif direction=="L":
            self.motors.turn_left()

# create the Robot instance.
ma=Robotfighter()

# get the time step of the current world.
timestep = int(ma.getBasicTimeStep())
while ma.step(timestep) != -1:
    ma.run("F")
    print(ma.distances.getDistanceValue())
    print(ma.positions.getPositionValue())
pass

    # ma.go()
    # ma.go_front()
    # ma.go_turnright()
    # ma.go_turnleft()