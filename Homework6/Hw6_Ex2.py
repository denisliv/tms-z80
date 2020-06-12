from Homework6 import Window
from time import time, sleep
from abc import abstractmethod, ABC
from math import sqrt
import random

window = Window.Window(100, 100, 600, 600) # Создание окна 600*600
fps = 60


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self): ...

    @abstractmethod
    def top(self) -> float: ...

    @abstractmethod
    def bottom(self) -> float: ...

    @abstractmethod
    def left(self) -> float: ...

    @abstractmethod
    def right(self) -> float: ...


class Rectangle(Shape):  # прямоугольник
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        window.draw_rectangle((self.x - 0.5*self.width, self.y - 0.5*self.height),
                              (self.width, self.height),
                              color='black')

    def top(self):
        return self.y - 0.5*self.height

    def bottom(self):
        return self.y + 0.5*self.height

    def left(self):
        return self.x - 0.5*self.width

    def right(self):
        return self.x + 0.5*self.width

    # @classmethod
    # def input(cls):
    #     w, h = int(input())
    #     return Rectangle()


class Square(Rectangle):  # квадрат
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.size = size

    def draw(self):
        window.draw_rectangle((self.x - 0.5 * self.size, self.y - 0.5 * self.size),
                              (self.size, self.size),
                              color='red')

    def top(self):
        return self.y - 0.5 * self.size

    def bottom(self):
        return self.y + 0.5 * self.size

    def left(self):
        return self.x - 0.5 * self.size

    def right(self):
        return self.x + 0.5 * self.size

    # @classmethod
    # def input(cls):
    #     w, h = int(input())
    #     return Rectangle()


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        window.draw_ellipse((self.x - self.radius, self.y - self.radius),
                              (self.radius, self.radius),
                              color='green')

    def top(self):
        return self.y - self.radius

    def bottom(self):
        return self.y + self.radius

    def left(self):
        return self.x - self.radius

    def right(self):
        return self.x + self.radius

    # @classmethod
    # def input(cls):
    #     w, h = int(input())
    #     return Rectangle()


class Triangle(Shape):  # равносторонний треугольник
    def __init__(self, x, y, height):
        super().__init__(x, y)
        self.height = height
        self.x = x
        self.y = y
        self.points = []

    def draw(self):
        self.points = [(self.x, self.y - 0.5 * self.height),
                       (self.x - self.height / sqrt(3), self.y),
                       (self.x + self.height / sqrt(3), self.y)]
        window.draw_polygon(*self.points, color='blue')

    def top(self):
        return self.y - 0.5*self.height

    def bottom(self):
        return self.y + 0.5*self.height

    def left(self):
        return self.x - self.height/sqrt(3)

    def right(self):
        return self.x + self.height/sqrt(3)

    # @classmethod
    # def input(cls):
    #     w, h = int(input())
    #     return Rectangle()


rect = Rectangle(400, 300, 40, 60)
square = Square(500, 600, 80)
circle = Circle(350, 280, 75)
triangle = Triangle(350, 280, 90)

velocity_rx = 4
velocity_ry = 6
velocity_sx = 8
velocity_sy = 10
velocity_cx = 5
velocity_cy = 7
velocity_tx = 10
velocity_ty = 15
while not window.closed:
    # frame start
    start = time()
    window.clear()

    rect.x += velocity_rx
    rect.y += velocity_ry
    square.x += velocity_sx
    square.y += velocity_sy
    circle.x += velocity_cx
    circle.y += velocity_cy
    triangle.x += velocity_tx
    triangle.y += velocity_ty

    if rect.right() > window.width:
        velocity_rx = -4
    elif rect.left() < 0:
        velocity_rx= 4

    if rect.bottom() > window.height:
        velocity_ry= -4
    elif rect.top() < 0:
        velocity_ry = 4

    if square.right() > window.width:
        velocity_sx = -8
    elif square.left() < 0:
        velocity_sx = 8

    if square.bottom() > window.height:
        velocity_sy = -10
    elif square.top() < 0:
        velocity_sy = 10

    if circle.right() > window.width:
        velocity_cx = -5
    elif circle.left() < 0:
        velocity_cx = 5

    if circle.bottom() > window.height:
        velocity_cy = -7
    elif circle.top() < 0:
        velocity_cy = 7

    if triangle.right() > window.width:
        velocity_tx = -10
    elif triangle.left() < 0:
        velocity_tx = 10

    if triangle.bottom() > window.height:
        velocity_ty = -15
    elif triangle.top() < 0:
        velocity_ty = 15

    rect.draw()
    square.draw()
    circle.draw()
    triangle.draw()
    window.update()  # flush draw commands

    # normalize fps
    pause = 1 / fps - (time() - start)
    if pause > 0:
        sleep(pause)



