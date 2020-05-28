from math import pi

class shapes:
    def __init__(self):
        print("All shapes are inherited directly or indirectly from shapes class")


class ellipse(shapes):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def perimeter(self):
        p = 2 * pi * (((self.a ** 2 + self.b ** 2) / 2) ** 0.5)
        return p

    def area(self):
        A = pi * self.a * self.b
        return (A)



class circle(ellipse):
    def __init__(self, r):
        self.a = r
        self.b = r

    def area(self):
        return super().area()


    def perimeter(self):
        return super().perimeter()

class non_circular(shapes):
    def __init__(self):
        pass
    pass


class triangle(non_circular):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = (a + b + c) / 2

    def area(self):
        a = (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5
        return a

    def perimeter(self):
        return 2 * self.s

class foursided(non_circular):
    def __init__(self):
        print("All four sided shapes are derived from non-circular shapes class")

    def perimeter(self):
        return 2 * (self.a + self.b)

class rectangle(foursided):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return super().perimeter()


class square(rectangle):
    def __init__(self, s):
        self.a = s
        self.b = s

    def area(self):
        return super().area()

    def perimeter(self):
        return super().perimeter()


class parallelogram(foursided):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def perimeter(self):
        return super().perimeter()


class hexagon(non_circular):
    def __init__(self, a):
        self.a = a

    def area(self):
        return 3 / 2 * (3 ** 0.5) * self.a * self.a

    def perimeter(self):
        return 6 * self.a


c = circle(5)
print(f"Circumference of circle is {c.perimeter()}")
print(f"Area of circle is {c.area()}")

e = ellipse(5,5)
print(f"Circumference of ellipse is {e.perimeter()}")   #done
print(f"Area of ellipse is {e.area()}")

t = triangle(3,4,5)
print(f"Perimeter of triangle is {t.perimeter()}")      #done
print(f"Area of triangle is {t.area()}")                #done

r = rectangle(4,5)
print(f"Perimeter of rectangle is {r.perimeter()}")
print(f"Area of rectangle is {r.area()}")                #done

s = square(5)
print(f"Perimeter of square is {s.perimeter()}")
print(f"Area of square is {s.area()}")

p = parallelogram(4,5)
print(f"Perimeter of parallelogram is {p.perimeter()}")

h = hexagon(8)
print(f"Perimeter of hexagon is {h.perimeter()}")
print(f"Area of hexagon is {h.area()}")

