import tkinter
from abc import ABC, abstractmethod
from tkinter import *
import math


class ConvexPolygon(ABC):
    @abstractmethod
    def __init__(self, fill_color, outline_colour):
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
        return getattr(self.fill_colour, self.otuline_colour)


# deskryptor
class Quantity:
    _count = 0  # zlicza liczbę instancji deskryptora

    def __init__(self):
        cls = self.__class__  # odwołanie do klasy deskryptora
        prefix = cls.__name__
        index = cls._count
        # unikalan wartość atrybutu storage_name dla każdej instancji deskryptora
        self.storage_name = f'_{prefix}#{index}'
        cls._count += 1

    # implementujemy __get__ bo nazwa atrybuty zarządzanego jest inna niż storage_name
    def __get__(self, instance, owner):  # owner - odwołanie do klasy zarządzanej
        return getattr(instance, self.storage_name)  # !

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)  # !
        else:
            raise ValueError("wartość musi być większa od zera!")


class Triangle(ConvexPolygon):
    base = Quantity()
    height = Quantity()

    def __init__(self):
        super(Triangle, self).__init__("yellow", "red")
        self.tuplePoints = ()

    def area(self):
        triangleArea = math.fabs(
            self.tuplePoints[0] * (self.tuplePoints[3] - self.tuplePoints[5]) + self.tuplePoints[2] *
            (self.tuplePoints[5] - self.tuplePoints[1]) + self.tuplePoints[4] * (
                        self.tuplePoints[1] - self.tuplePoints[3])) / 2
        return round(triangleArea, 2)

    def perimeter(self):
        AB = math.sqrt(
            math.pow(self.tuplePoints[2] - self.tuplePoints[0], 2) + math.pow(self.tuplePoints[3] - self.tuplePoints[1],
                                                                              2))
        BC = math.sqrt(
            math.pow(self.tuplePoints[4] - self.tuplePoints[2], 2) + math.pow(self.tuplePoints[5] - self.tuplePoints[3],
                                                                              2))
        CA = math.sqrt(
            math.pow(self.tuplePoints[0] - self.tuplePoints[4], 2) + math.pow(self.tuplePoints[1] - self.tuplePoints[5],
                                                                              2))
        return round(AB + BC + CA, 2)

    def draw(self):
        Window(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

#done
class IsoscelesTriangle(Triangle):
    def __init__(self, window):
        super(IsoscelesTriangle, self).__init__()


    def getData(self):
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)


        self.button_1.grid(row=3, column=1)


    def draw(self):
        marginX = 100
        marginY = 200
        self.height = float(self.entry_1.get())
        self.base = float(self.entry_2.get())

        self.tuplePoints = (
            marginX, marginY, self.base + marginX, marginY, (self.base / 2) + marginX, -self.height + marginY, marginX,
            marginY)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())


#done
class EquilateralTriangle(Triangle):
    Sidea = Quantity()
    def __init__(self, window):
        super(EquilateralTriangle, self).__init__()

    def getData(self):
        print("tworzenie trójkąta równoramiennego")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość podstawy: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.button_1.grid(row=3, column=1)

    def draw(self):
        marginX = 200
        marginY = 300
        self.base = float(self.entry_1.get())
        self.height = (self.base * math.sqrt(3)) / 2
        self.tuplePoints = (
            marginX, marginY, self.base + marginX, marginY, (self.base / 2) + marginX, -self.height + marginY, marginX,
            marginY)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())



#done
class RegularPentagon(ConvexPolygon):
    Side = Quantity()
    def __init__(self, window):
        super(RegularPentagon,self).__init__("green", "blue")
        self.tuplePoints = ()


    def area(self):
        return round(3 * (self.Side ** 2 / 4) * (1 / math.tan(math.radians(36))),2)
    def perimeter(self):
        return round(5 * self.Side,2)
    def draw(self):
        marginX = 300
        marginY = 150
        self.Side = float(self.entry_1.get())
        tab = list()
        for i in range(5):
            x = marginX + self.Side * math.cos(math.radians(360 / 5 * i))
            y = marginY + self.Side * math.sin(math.radians(360 / 5 * i))
            tab.append([x, y])
        self.tuplePoints = tuple(tab)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie pięciokąta foremnego")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.button_1.grid(row=3, column=1)


#done
class RegularHexagon(ConvexPolygon):
    Side = Quantity
    def __init__(self,window):
        super(RegularHexagon,self).__init__("pink","red")
        self.tuplePoints = ()


    def area(self):
        return round((3*math.pow(self.Side,2)*math.sqrt(3))/2,2)

    def perimeter(self):
        return round(6 * self.Side, 2)

    def draw(self):
        marginX = 300
        marginY = 150
        self.Side = float(self.entry_1.get())
        tab = list()
        for i in range(6):
            x = marginX + self.Side * math.cos(math.radians(360 / 6 * i))
            y = marginY + self.Side * math.sin(math.radians(360 / 6 * i))
            tab.append([x, y])
        self.tuplePoints = tuple(tab)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie sześciokąta foremnego")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.button_1.grid(row=3, column=1)


#done
class RegularOctagon(ConvexPolygon):
    Side = Quantity
    def __init__(self, window):
        super(RegularOctagon,self).__init__("pink","red")
        self.tuplePoints = ()


    def area(self):
        return round(2 * (1 + math.sqrt(2)) * math.pow(self.Side,2),2)

    def perimeter(self):
        return round(8 * self.Side, 2)

    def draw(self):
        marginX = 300
        marginY = 150
        self.Side = float(self.entry_1.get())
        tab = list()
        for i in range(8):
            x = marginX + self.Side * math.cos(math.radians(360 / 8 * i))
            y = marginY + self.Side * math.sin(math.radians(360 / 8 * i))
            tab.append([x, y])
        self.tuplePoints = tuple(tab)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie ośmiokąta foremnego")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.button_1.grid(row=3, column=1)

#done
class Rhombus(ConvexPolygon):
    Side = Quantity()
    angle = Quantity()
    def __init__(self, window):
        super(Rhombus,self).__init__("#FF337A","#33C1FF")
        self.tuplePoints = ()

    def area(self):
        return round(math.pow(self.Side,2) * math.sin(math.radians(self.angle)),2)

    def perimeter(self):
        return round(4*self.Side,2)

    def draw(self):
        marginX = 200
        marginY = 150
        self.Side = float(self.entry_1.get())
        self.angle = float(self.entry_2.get())
        cos = math.cos(self.angle) * self.Side
        sin = math.sin(self.angle) * self.Side
        self.tuplePoints = (marginX, marginY,
                            marginX + self.Side, marginY,
                            marginX + self.Side + cos, marginY + sin,
                            marginX + cos, marginY + sin)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie rąbu")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość a: ")
        self.entry_1 = Entry(root)

        self.label_2 = Label(root, text="podaj kąt α:: ")
        self.entry_2 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.label_2.grid(row=1, column=0)
        self.entry_2.grid(row=1, column=1)


        self.button_1.grid(row=3, column=1)

#done
class Square(Rhombus):
    Side = Quantity()
    def __init__(self, window):
        super(Square, self).__init__(window)


    def area(self):
        return round(pow(self.Side,2), 2)

    def perimeter(self):
        return round(4 * self.Side, 2)

    def draw(self):
        marginX = 150
        marginY = 250
        self.Side = float(self.entry_1.get())
        self.tuplePoints = (marginX, marginY,
                            self.Side + marginX, marginY,
                            marginX + self.Side, marginY - self.Side, marginX,
                            marginY - self.Side, marginX, marginY)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())
    def getData(self):
        print("tworzenie kwadratu")
        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku a: ")
        self.entry_1 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.button_1.grid(row=3, column=1)

#done
#rownoleglobok
class Parallelogram(Rhombus):
    SideA = Quantity()
    SideB = Quantity()
    angle = Quantity()
    def __init__(self,window):
        super(Parallelogram, self).__init__(window)

    def perimeter(self):
        return 2 * self.SideA + 2 * self.SideB

    def area(self):
        return round(self.SideA * self.SideB * math.sin(math.radians(self.angle)),2)

    def draw(self):
        marginX = 50
        marginY = 100
        self.SideA = float(self.entry_1.get())
        self.SideB = float(self.entry_2.get())
        self.angle = float(self.entry_3.get())
        a_cos = math.cos(math.radians(self.angle)) * self.SideA
        b_sin = math.sin(math.radians(self.angle)) * self.SideB

        self.tuplePoints = (marginX, marginY,
                            marginX + self.SideA + self.SideB, marginY,
                            marginX + self.SideA + a_cos + self.SideB, marginY + b_sin,
                            marginX + a_cos, marginY + b_sin)
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())


    def getData(self):
        print("tworzenie równoległoboku")

        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość boku a: ")
        self.entry_1 = Entry(root)

        self.label_2 = Label(root, text="podaj długość boku b: ")
        self.entry_2 = Entry(root)

        self.label_3 = Label(root, text="podaj kąt α")
        self.entry_3 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.label_2.grid(row=1, column=0)
        self.entry_2.grid(row=1, column=1)

        self.label_3.grid(row=2, column=0)
        self.entry_3.grid(row=2, column=1)

        self.button_1.grid(row=3, column=1)


#done
#kwadrat
class Rectangle(Parallelogram):
    SideA = Quantity()
    SideB = Quantity()
    def __init__(self,window):
        super(Rectangle, self).__init__(window)

    def perimeter(self):
        return 2 * self.SideA + 2 * self.SideB

    def area(self):
        return self.SideA * self.SideB

    def draw(self):
        marginX = 150
        marginY = 100
        self.SideA = float(self.entry_1.get())
        self.SideB = float(self.entry_2.get())
        self.tuplePoints = (marginX, marginY,
                            marginX + self.SideA, marginY,
                            marginX + self.SideA, marginY + self.SideB,
                            marginX, marginY + self.SideB
                            )
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie prostokąta")

        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość a: ")
        self.entry_1 = Entry(root)

        self.label_2 = Label(root, text="podaj długość boku b: ")
        self.entry_2 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.label_2.grid(row=1, column=0)
        self.entry_2.grid(row=1, column=1)

        self.button_1.grid(row=3, column=1)


# deltoid
class Kite(ConvexPolygon):
    Side = Quantity()
    angleA = Quantity()
    angleB = Quantity()
    p = Quantity()
    SideA = Quantity()
    SideB = Quantity()
    def __init__(self,window):
        super(Kite, self).__init__("red","black")
        self.tuplePoints = ()

    def perimeter(self):
        return round(2*self.SideA+2*self.SideB,2)

    def area(self):
        return round(self.p*self.Side/2,2)

    def draw(self):
        marginX = 200
        marginY = 100
        self.Side = float(self.entry_1.get())
        self.angleA = float(self.entry_2.get())
        self.angleB = float(self.entry_3.get())

        angleAhalf = self.angleA / 2
        angleBhalf = self.angleB / 2
        a = 1 / math.sin(math.radians(angleAhalf)) * (self.Side / 2)
        b = 1 / math.sin(math.radians(angleBhalf)) * (self.Side / 2)
        x = math.cos(math.radians(angleAhalf)) * a
        y = 1 / math.tan(math.radians(angleBhalf)) * (self.Side / 2)
        self.p = x + y
        self.SideA = a
        self.SideB = b
        self.tuplePoints = (marginX, marginY,
                            marginX + (self.Side / 2), marginY + x,
                            marginX, marginY + y,
                            marginX - (self.Side / 2), marginY + x,
                            )
        window.initUI(self.tuplePoints, self.fill_colour, self.otuline_colour, self.area(), self.perimeter())

    def getData(self):
        print("tworzenie deltoidu")


        root = tkinter.Tk()
        self.label_1 = Label(root, text="podaj długość przekątnej: ")
        self.entry_1 = Entry(root)

        self.label_2 = Label(root, text="podja kąt α: ")
        self.entry_2 = Entry(root)

        self.label_3 = Label(root, text="podaj kąt b")
        self.entry_3 = Entry(root)

        self.button_1 = Button(root, text="Rysuj!", command=self.draw)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)

        self.label_2.grid(row=1, column=0)
        self.entry_2.grid(row=1, column=1)

        self.label_3.grid(row=2, column=0)
        self.entry_3.grid(row=2, column=1)

        self.button_1.grid(row=3, column=1)



class Window(Frame):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=400, height=400, background="bisque")


    def initUI(self, tupleOfTops, fill_color, outline_colour, area, perimeter):

        self.canvas.delete(ALL)
        frame = Frame(self.canvas, bg='purple')
        self.canvas.create_window((0, 0), window=frame, anchor=NW)

        self.pack(fill=BOTH, expand=True)
        self.canvas.create_polygon(tupleOfTops, outline=outline_colour,fill=fill_color, width=2)
        # canvas.create_line(self.tupleOfTops)
        self.canvas.create_text(110, 10, font="italic", text=f"Area: {area}, Perimeter:{perimeter}")
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=1,padx=0, sticky=E + W + S + N)


    def menu(self,ww):
        self.master.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)

        abtn = Button(self, text="Activate", command=Kite(self).getData)
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close", command=ww.initUI)
        cbtn.grid(row=2, column=3, pady=4)


# t_rownoramienny = IsoscelesTriangle()


w = Tk()

window = Window()
window.menu(window)

# t_rownoramienny.getData()

w.geometry("600x450+200+200")
w.mainloop()
