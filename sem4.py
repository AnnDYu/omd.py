# Задание #1: создать класс Color и красить точку в разные цвета
class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{Color.START};{self.red};{self.green};{self.blue}{Color.MOD}●{Color.END}{Color.MOD}'

    # Задание #2: сравнение цветов
    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue


    # Задание #3: реализуйте смешивание цветов через сложение экземпляров класса Color
    def __add__(self, other):
        if not isinstance(other, Color):
            raise ArithmeticError("Elements should be colors")
        return Color(min(self.red + other.red, 255),
                     min(self.green + other.green, 255),
                     min(self.blue + other.blue, 255))

    # Задание #4: Из списка цветов оставьте уникальные
    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    # Задание #5: Реализуйте уменьшение контраста умножением на с = [0, 1] экземпляра класса Color
    @staticmethod
    def brightness(color, c: float):
        cl = - 256 *(1-c)
        f = (256 * (cl + 255))/ (255 * (259 - cl))
        lr = int(f * (color - 128) + 128)
        return lr

    def __mul__(self, c: float):
        return Color(Color.brightness(self.red, c),Color.brightness(self.blue, c),Color.brightness(self.green, c))

    __rmul__ = __mul__


def main():
    red = Color(255, 0, 0)
    print(red)
    red1 = Color(255, 0, 0)
    red2 = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(id(red1))
    print(id(red2))
    print(red + green)
    color_list = [red, green, red1]
    print(set(color_list))
    print(0.5 * red)


if __name__ == '__main__':
    main()
