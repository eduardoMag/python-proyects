class Circle1:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else:
            raise ValueError("value must be positive")

    def area(self):
        return 3.14159 * (self.__radius ** 2)


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    def __setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else:
            raise ValueError("Value must be positive")

    radius = property(None, __setRadius)

    @property
    def area(self):
        return 3.14159 * (self.__radius ** 2)


# testing Circle1
c1 = Circle1(42)
print(c1.area())
# print(c1.__radius)

c1.setRadius(66)
print(c1.area())

# c1.setRadius(-4)


# testing Circle2
c2 = Circle2(42)
print(c2.area)
# print(c2.radius)
c2.radius = 12
print(c2.area)
# c2.radius = -4
