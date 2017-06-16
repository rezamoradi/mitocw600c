# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:


class Shape(object):
    def area(self):
        raise AttributeError("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side**2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#


class Triangle(Shape):
    def __init__(self, base, height):
        """
        h: length of side of the square
        """
        self.base = float(base)
        self.height = float(height)

    def area(self):
        """
        Returns area of the square
        """
        return self.base * self.height / 2

    def __str__(self):
        return 'Triangle with base %0.1f and height %0.1f' % (self.base, self.height)


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.


class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shapes = []
        self.place = None

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh not in self.shapes:
            self.shapes.append(sh)
        else:
            print(sh, end=' ')
            print('is already in the set.')

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self

    def __next__(self):
        if self.place >= len(self.shapes):
            raise StopIteration
        self.place += 1
        return self.shapes[self.place - 1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        return '\n'.join([shape.__str__() for shape in self.shapes])
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#


def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    shape_area = [shape.area() for shape in shapes]
    max_area = max(shape_area)

    return tuple(shape for shape in shapes if shape.area() == max_area)

#
# Problem 4: Read shapes from a file into a ShapeSet
#


def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    file = open(filename, 'r')
    shapes = ShapeSet()
    for line in file:
        spec = line.strip().split(',')
        if spec[0] == 'square':
            shape = Square(float(spec[1]))
            shapes.addShape(shape)
        elif spec[0] == 'circle':
            shape = Circle(float(spec[1]))
            shapes.addShape(shape)
        elif spec[0] == 'triangle':
            shape = Triangle(float(spec[1]), float(spec[2]))
            shapes.addShape(shape)

    return shapes


if __name__ == '__main__':
    a = Square(2)
    b = Square(1)
    c = Circle(1)
    t = Triangle(4, 2)
    ss = ShapeSet()
    ss.addShape(a)
    ss.addShape(b)
    ss.addShape(c)
    ss.addShape(t)

    for sh in ss:
        print(sh)

    print('==========================')

    for sh in findLargest(ss):
        print(sh)

    print('==========================')

    ss = readShapesFromFile('shapes.txt')
    print(ss)