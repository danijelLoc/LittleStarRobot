import turtle
import math
import random


class StarRobot:

    def __init__(self):
        self.ws = turtle.Screen()
        self.ws.colormode(255)
        self.geekyTurtle = turtle.Turtle()
        self.geekyTurtle.speed(speed="fastest")

    def enableWriting(self):
        self.geekyTurtle.pencolor("green")
        self.randomColor()
        self.geekyTurtle.pendown()

    def randomColor(self):
        random_color = tuple([random.randint(0, 255) for i in range(3)])
        self.geekyTurtle.pencolor(random_color)

    def disableWriting(self):
        # self.geekyTurtle.pencolor("red")
        self.geekyTurtle.penup()

    def drive(self, distance: float):
        self.geekyTurtle.forward(distance)

    def turn(self, angle: float):
        self.geekyTurtle.right(angle)

    def draw_arm(self, arm_length: float, inner_polygon_side_length: float):
        self.enableWriting()
        try:
            gamma = math.degrees(math.acos((inner_polygon_side_length / 2) / arm_length))
        except ValueError:
            self.disableWriting()
            return
        delta = (180 - 2 * gamma)
        self.turn(gamma)
        self.drive(arm_length)
        self.turn(-(180 - delta))
        self.drive(arm_length)
        self.disableWriting()
        self.turn(-180)
        self.turn(gamma)
        self.drive(inner_polygon_side_length)
        self.turn(-180)

    def draw_filled_arm(self, arm_length: float, inner_polygon_side_length: float):
        arm_len = arm_length
        inner_polygon_side_len = inner_polygon_side_length
        while arm_len > 0:
            self.draw_arm(arm_len, inner_polygon_side_len)
            arm_len -= 10.0

    def draw(self, number_of_arms: int, inner_radius: float, arm_length: float):
        self.disableWriting()
        alpha = 360.0 / number_of_arms
        beta = (180 - alpha) / 2
        inner_polygon_side_length = math.sin(math.radians(alpha / 2)) * inner_radius * 2
        self.drive(inner_radius)
        self.turn(-(180 - beta))
        for i in range(number_of_arms):
            self.draw_filled_arm(arm_length, inner_polygon_side_length)
            self.drive(inner_polygon_side_length)
            self.turn(-(180 - 2 * beta))
