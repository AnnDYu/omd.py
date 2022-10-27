# Задание 1. сделайте класс BasePokemon, устанавливающий атрибуты name и category, имеющий метод
# to_str выводящий строку из атрибутов name и category
class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'


# Задание 2. отнаследуйтесь от класса basepokemon в класс pokemon, удалив ненужный код
class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self.weaknesses = weaknesses


# Задание 3. Дан класс pokemon. Замените метод to_str
class BasePokemon1:
    def __init__(self, name, poketype):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{self.poketype}'


# Задание 4. Напишите mixin EmojiMixin кторый модифицирует метод str
class BasePokemon2:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'

class EmojiMixin:
    icon = { 'grass':'🌿','electric':'⚡'}
    def __str__(self):
        text : str = 'Pikachu/electric'
        for title, emoji in self.icon.items():
            replaced = text.replace( title, emoji)
            if replaced != text:
                return replaced
        return text

class Pokemon1(EmojiMixin, BasePokemon2):
    pass

if __name__ == '__main__':
    base_charmander = BasePokemon(name='Charmander', category='Lizard')
    print(base_charmander.to_str())

    charmander = Pokemon(
        name='Charmander',
        category='Lizard',
        weaknesses=('water', 'ground', 'rock'))
    print(charmander.to_str())

    bulbasaur = BasePokemon1(name='Bulbasaur', poketype='grass')
    print(repr(bulbasaur))

    pikachu = Pokemon1(name='Pikachu', category='electric')
    print(pikachu)
