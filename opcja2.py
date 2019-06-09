from abc import ABC, abstractmethod
from tkinter import Tk, Canvas, Frame, BOTH
import math


class ConvexPolygon(ABC):
    @abstractmethod
    def __init__(self, fill_color, outline_colour):
        self.fill_colour = fill_color
        self.outline_colour = outline_colour
        super(ConvexPolygon, self).__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def __get__(self, instance, owner):
        return getattr(self.fill_colour, self.outline_colour)


class ConvexQuadrilateral(ConvexPolygon):
    def __init__(self):
        super(ConvexQuadrilateral, self).__init__("yellow", "blue")
        self.diagonalA = 0
        self.diagonalB = 0
        self.crossDg = 0
        self.tuplePoints = ()

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        Window(self.tuplePoints, self.fill_colour, self.outline_colour)
        pass


class Square(ConvexQuadrilateral):
    def __init__(self):
        super(Square, self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie kwadratu")
        print("podaj długość przekątnej: ")
        b = input()
        self.diagonalA = float(b)
        self.diagonalB = float(b)
        self.crossDg = 90

    def topCalculator(self):
        marginX = 150
        marginY = 300
        sideWidth = math.sqrt(math.pow(self.diagonalA / 2, 2) + math.pow(self.diagonalB / 2, 2))
        self.tuplePoints = (
            marginX, marginY, sideWidth + marginX, marginY, marginX + sideWidth, marginY - sideWidth, marginX,
            marginY - sideWidth, marginX, marginY)


class Rectangle(ConvexQuadrilateral):
    def __init__(self):
        super(Rectangle, self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie prostokąta")
        print("podaj długość przekątnej d1: ")
        a = input()
        print("podaj długość przekątnej d2: ")
        b = input()
        print ("Podaj kąt przecięcia przekątnych: ")
        c = input()
        self.diagonalA = float(a)
        self.diagonalB = float(b)
        c = float(c)
        self.crossDg = math.radians(c)

    def topCalculator(self):
        marginX = 150
        marginY = 300
        halfWidthD1 = self.diagonalA / 2
        halfWidthD2 = self.diagonalB / 2
        sideBWidth = math.sqrt(math.pow(halfWidthD1, 2) + math.pow(halfWidthD2, 2) - (
                2 * halfWidthD1 * halfWidthD2 * math.cos(self.crossDg)))
        sideAWidth = math.sqrt(math.pow(halfWidthD1, 2) + math.pow(halfWidthD2, 2) - (
                2 * halfWidthD1 * halfWidthD2 * math.cos(math.radians(180) - self.crossDg)))
        self.tuplePoints = (
            marginX, marginY, marginX + sideAWidth, marginY, marginX + sideAWidth, marginY - sideBWidth, marginX,
            marginY - sideBWidth, marginX, marginY)


class Rhombus(ConvexQuadrilateral):
    def __init__(self):
        super(Rhombus, self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie rombu")
        print("podaj przekątną d1: ")
        a = input()
        print("Podaj przekątną d1: ")
        b = input()
        self.diagonalA = float(a)
        self.diagonalB = float(b)
        self.crossDg = 90

    def topCalculator(self):
        marginX = 150
        marginY = 200
        halfWidthD1 = self.diagonalA / 2
        halfWidthD2 = self.diagonalB / 2
        sideWidth = math.sqrt(math.pow(halfWidthD1, 2) + math.pow(halfWidthD2, 2))
        height = self.area() / sideWidth
        movement = math.sqrt(math.pow(sideWidth, 2) - math.pow(height, 2))

        self.tuplePoints = (
            marginX, marginY, marginX + sideWidth, marginY, marginX + sideWidth + movement, marginY - height,
            marginX + movement, marginY - height, marginX, marginY)

    def area(self):
        return (self.diagonalA * self.diagonalB) / 2


class Parallelogram(ConvexQuadrilateral):
    def __init__(self):
        super(Parallelogram, self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie równoległoboku")
        print("podaj przekątną d1: ")
        a = input()
        print("podaj przekątną d2: ")
        b = input()
        print("podaj kąt przecięcia przekątnych: ")
        c = input()
        self.diagonalA = float(a)
        self.diagonalB = float(b)
        c = float(c)
        self.crossDg = math.radians(c)
        print(math.cos(self.crossDg))

    def topCalculator(self):
        marginX = 150
        marginY = 200
        halfWidthD1 = self.diagonalA / 2
        halfWidthD2 = self.diagonalB / 2
        sideBWidth = math.sqrt(math.pow(halfWidthD1, 2) + math.pow(halfWidthD2, 2) - (
                        2 * halfWidthD1 * halfWidthD2 * math.cos(self.crossDg)))
        sideAWidth = math.sqrt(math.pow(halfWidthD1, 2) + math.pow(halfWidthD2, 2) - (
                        2 * halfWidthD1 * halfWidthD2 * math.cos(math.radians(180) - self.crossDg)))
        print(sideBWidth)
        height = self.area()/sideAWidth
        movement = math.sqrt(math.pow(sideBWidth, 2) - math.pow(height, 2))
        self.tuplePoints = (
            marginX, marginY, marginX + sideAWidth, marginY, marginX + sideAWidth - movement, marginY - height,
            marginX - movement, marginY - height, marginX, marginY)

    def area(self):
        if self.crossDg >= 90:
            return (self.diagonalA * self.diagonalB * math.cos(self.crossDg))/2
        else:
            return (self.diagonalA * self.diagonalB * math.cos(180 - self.crossDg))/2


class Window(Frame):

    def __init__(self, tupleOfTops, fill_color, outline_colour):
        super().__init__()
        self.fill_color = fill_color
        self.outline_colour = outline_colour
        self.tupleOfTops = tupleOfTops
        self.initUI()

    def initUI(self):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_polygon(self.tupleOfTops, outline=self.outline_colour,
                              fill=self.fill_color, width=2)
        # canvas.create_line(self.tupleOfTops)

        canvas.pack(fill=BOTH, expand=1)


shape = Rectangle()
w = Tk()

shape.draw()
shape.area()
shape.perimeter()

w.geometry("600x350+300+300")
w.mainloop()
