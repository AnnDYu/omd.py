class CountVectorizer:
    """преобразовывает массив с предложениями в 2 матрицы"""
    def __init__(self):
        self.words = []
        self.matrix = []

    def fit_transform(self, some_text: list[str]) -> list:
        """преобразует начальный массив в массив из массивов с колличеством слов для каждого предложения"""
        mat = []
        for sentence in some_text:
            one = sentence.split()
            for word in one:
                word = word.lower()
                if word not in self.words:
                    self.words.append(word)
        for sentence in some_text:
            one = str(sentence.split()).lower()
            for uniq_word in self.words:
                number = one.count(uniq_word)
                mat.append(number)
            self.matrix.append(mat)
            mat = []
        return self.matrix

    def get_feature_names(self) -> list[str]:
        """возвращает массив уникальных слов из всех предложений"""
        return self.words


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
