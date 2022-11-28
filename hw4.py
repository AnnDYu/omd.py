from typing import Dict
import json


class ColorizeMixin():
    """миĸсин ColorizeMixin. меняет цвет теĸста при выводе на ĸонсоль"""
    def __init__(self, repr_color_code):
        self.repr_color_code = 33  # yellow


class Advert(ColorizeMixin):
    """ динамически создает атрибуты экземпляра класса из атрибутов JSON-объекта """
    repr_color_code = 33

    def __init__(self, data: json) -> object:
        for key, value in data.items():
            if isinstance(value, dict):
                value = Advert(value)
            if key == 'price':
                self._price = value
            elif key == 'class':
                self.class_ = value
            else:
                setattr(self, key, value)

    @property
    def price(self):
        if hasattr(self, '_price'):
            if self._price < 0:
                raise ValueError('price must be >= 0')
            else:
                return self._price
        else:
            return 0

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};10m {self.title} | {self._price} ₽  \n'


if __name__ == '__main__':
    lesson_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }"""
    lesson = json.loads(lesson_str)
    print(lesson)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad._price)
    print(lesson_ad.class_)
    print(lesson_ad)
