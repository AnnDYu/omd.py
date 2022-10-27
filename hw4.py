import json5


class ColorizeMixin():
    # миĸсин ColorizeMixin меняет цвет теĸста при выводе на ĸонсоль
    def __init__(self, repr_color_code):
        self.repr_color_code = 33  # yellow


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, data: json5) -> object:
        for key, value in data.items():
            if isinstance(value, dict):
                value = Advert(value)
            if key == 'price':
                self._price = value
                if self._price < 0:
                    raise ValueError('price must be >= 0')
            elif key == 'class':
                self.class_ = value
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};10m {self.title} | {self._price} ₽  \n'


lesson_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

if __name__ == '__main__':
    lesson = json5.loads(lesson_str)
    print(lesson)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad._price)
    print(lesson_ad.class_)
    print(lesson_ad)
