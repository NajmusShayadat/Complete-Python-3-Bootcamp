# Object Oriented Programming
# Homework Assignment

# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x_dis = coor2[0] - coor1[0]
        self.y_dis = coor2[1] - coor1[1]

    def distance(self):
        # distance  = sqrt( (x1 -x2)^2 + (y1 - y2)^2)
        return (self.y_dis ** 2 + self.x_dis ** 2) ** 0.5

    def slope(self):
        # slope = (y2 - y1) / (x2 -x1)
        if self.x_dis != 0:
            return self.y_dis / self.x_dis
        else:
            return 0


# EXAMPLE OUTPUT
coordinate1 = (0, 0)
coordinate2 = (8, 8)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()


# Problem 2
# Fill in the class to return Volume and Surface area of a cylinder with given height and radius


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        # volume = pi * h * r^2
        return self.pi * self.height * (self.radius ** 2)

    def surface_area(self):
        # surface are = 2 * pi * h * r + 2 * pi * h * r^2
        return 2 * self.pi * self.radius * self.height + 2 * self.pi * (self.radius ** 2)


# EXAMPLE OUTPUT
c = Cylinder(2, 3)
c.volume()
c.surface_area()
