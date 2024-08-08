class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = [1] * self.sides_count if not sides else sides[:self.sides_count]
        self.__color = self.__is_valid_color(*color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return [r, g, b]
        else:
            return False

    def set_color(self, r, g, b):
        color = self.__is_valid_color(r, g, b)
        if color:
            self.__color = color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(side > 0 for side in new_sides):
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14 * self.get_sides()[0] ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *[side]*12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())

