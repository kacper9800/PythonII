from abc import ABC, abstractmethod
from tkinter import Tk, Canvas, Frame, BOTH
import math
class ConvexPolygon(ABC):
    @abstractmethod
    def __init__(self, fill_color,outline_colour):
        self.fill_colour = fill_color
        self.otuline_colour = outline_colour
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
        return getattr(self.fill_colour,self.otuline_colour)

class Triangle(ConvexPolygon):
    def __init__(self):
        super(Triangle, self).__init__("yellow", "red")
        self.base = 0
        self.height = 0
        self.tuplePoints = ()
    def area(self):

        triangleArea = math.fabs(self.tuplePoints[0]*(self.tuplePoints[3]-self.tuplePoints[5])+self.tuplePoints[2]*
              (self.tuplePoints[5]-self.tuplePoints[1])+self.tuplePoints[4]*(self.tuplePoints[1]-self.tuplePoints[3]))/2
        print("Pole: "+str(triangleArea)+"px^2")

    def perimeter(self):
        AB = math.sqrt(math.pow(self.tuplePoints[2]-self.tuplePoints[0],2) + math.pow(self.tuplePoints[3]-self.tuplePoints[1],2))
        BC = math.sqrt(math.pow(self.tuplePoints[4] - self.tuplePoints[2], 2) + math.pow(self.tuplePoints[5] - self.tuplePoints[3],2))
        CA = math.sqrt(math.pow(self.tuplePoints[0] - self.tuplePoints[4], 2) + math.pow(self.tuplePoints[1] - self.tuplePoints[5],2))
        print("Obwód: "+str(round(AB + BC + CA,2)))
    def draw(self):
        Window(self.tuplePoints,self.fill_colour ,self.otuline_colour)

    def __set__(self, instance, height, base):
        setattr(instance, self.height, self.base)


class IsoscelesTriangle(Triangle):
    def __init__(self):
        super(IsoscelesTriangle, self).__init__()
        self.getData()
        self.topCalculator()
    def getData(self):
        print("tworzenie trójkąta równoramiennego")
        print("podaj długość podstawy: ")
        b = input()
        self.base = float(b)
        print("podaj wysokość: ")
        h = input()
        self.height = float(h)
    def topCalculator(self):
        marginX = 150
        marginY = 300
        self.tuplePoints = (marginX,marginY,self.base+marginX,marginY,(self.base/2)+marginX,-self.height+marginY,marginX,marginY)



class EquilateralTriangle(Triangle):
    def __init__(self):
        super(EquilateralTriangle,self).__init__()
        self.getData()
        self.topCalculator()
    def getData(self):
        print("tworzenie trójkąta równoramiennego")
        print("podaj długość podstawy: ")
        b = input()
        self.base = float(b)
        self.height = (self.base*math.sqrt(3))/2
    def topCalculator(self):
        marginX = 150
        marginY = 300
        self.tuplePoints = (marginX,marginY,self.base+marginX,marginY,(self.base/2)+marginX,-self.height+marginY,marginX,marginY)

class ConvexQuadrilateral(ConvexPolygon):
    def __init__(self):
        super(ConvexQuadrilateral,self).__init__("yellow", "blue")
        self.SideA = 0
        self.SideB = 0
        self.SideC = 0
        self.tuplePoints = ()

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        Window(self.tuplePoints, self.fill_colour, self.otuline_colour)
        pass

# class Parallelogram(ConvexQuadrilateral):
#     def __init__(self):
#         super(Parallelogram, self).__init__()

class Square(ConvexQuadrilateral):
    def __init__(self):
        super(Square,self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie kwadratu")
        print("podaj długość boku: ")
        b = input()
        self.SideA = float(b)
        self.SideB = float(b)

    def topCalculator(self):
        marginX = 150
        marginY = 300
        self.tuplePoints = (marginX,marginY, self.SideA+marginX,marginY, marginX+self.SideA, marginY-self.SideA, marginX,marginY-self.SideA, marginX,marginY)


class Rectangle(ConvexQuadrilateral):
    def __init__(self):
        super(Rectangle,self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie prostokąta")
        print("podaj długość boku a: ")
        a = input()
        print("podaj długość boku b: ")
        b = input()
        self.SideA = float(a)
        self.SideB = float(b)


    def topCalculator(self):
        marginX = 150
        marginY = 300
        self.tuplePoints = (marginX,marginY, self.SideA+marginX,marginY, marginX+self.SideA,marginY - self.SideB, marginX,marginY-self.SideB, marginX,marginY)

class Rhombus(ConvexQuadrilateral):
    def __init__(self):
        super(Rhombus,self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie rombu")
        print("podaj bok e: ")
        e = input()
        # print("podaj przekątną f: ")
        # f = input()
        self.SideA = float(e)
        # self.SideB = float(f)

    def topCalculator(self):
        marginX = 150
        marginY = 200
        halfWidth = self.SideA/2
        # self.tuplePoints = (marginX,marginY, marginX+(self.SideA/2),marginY+(self.SideB/2), marginX+self.SideA,marginY, marginX+(self.SideA/2),marginY-(self.SideB/2), marginX,marginY)
        self.tuplePoints = (marginX,marginY+halfWidth, marginX-halfWidth,marginY ,marginX,marginY-halfWidth, marginX+halfWidth,marginY,marginX,marginY+halfWidth)


class Parallelogram(ConvexQuadrilateral):
    def __init__(self):
        super(Parallelogram,self).__init__()
        self.getData()
        self.topCalculator()

    def getData(self):
        print("tworzenie rombu")
        print("podaj bok a: ")
        a = input()
        print("podaj bok b: ")
        b = input()
        print("podaj wysokość h: ")
        h = input()
        self.SideA = float(a)
        self.SideB = float(b)
        self.SideC = float(h)
    def topCalculator(self):
        marginX = 150
        marginY = 200
        move = math.sqrt(math.pow(self.SideA,2) - math.pow(self.SideC,2))
        print(move)
        halfWidth = self.SideA/2
        self.tuplePoints = (marginX,marginY,
                            marginX+self.SideA+move,marginY,
                            marginX, marginY+self.SideC,
                            marginX-self.SideA-move, marginY+self.SideC,
                            marginX, marginY
                            )





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




# shape = IsoscelesTriangle()
# shape = EquilateralTriangle()
# shape = Square()
# shape = Rectangle()
# shape = Rhombus()
shape = Parallelogram()
w = Tk()


shape.draw()
shape.area()
shape.perimeter()

w.geometry("600x350+300+300")
w.mainloop()
