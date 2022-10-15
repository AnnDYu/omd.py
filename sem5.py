from math import log

class CountVectorizer:
    def __init__(self):
        self.words = []
        self.matrix = []
        pass

    def fit_transform(self, some_text: list[str]) -> list:
        mat = []
        for sentence in some_text:
            one = sentence.split()
            for word in one:
                word = word.lower()
                if word not in self.words:
                    self.words.append(word)
        for sentence in some_text:
            one = str(sentence.split()).lower()
            for uniqword in self.words:
                number = one.count(uniqword)
                mat.append(number)
            self.matrix.append(mat)
            mat = []
        return self.matrix

    def get_feature_names(self) -> list[str]:
        return self.words


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, matr: list[list[int]]) -> list[list[float]]:
        sum_word = 0
        freq_list = []
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number / sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list

    def idf_transform(self, matr: list[list[int]]) -> list[float]:
        column_len = len(matr[0])
        len_array = len(matr)
        idf = []
        for word_index in range(column_len):
            counter = 0
            for doc in matr:
                if doc[word_index] != 0:
                    counter += 1
            idf.append(log((len_array + 1) / (counter + 1)) + 1)
        return idf

    def fit_transform(self, matrix: list[list[int]]) -> list[list[float]]:
        tf = self.tf_transform(matrix)
        idf = self.idf_transform(matrix)

        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]
        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__() # это чтоб вызвать родительский код
        self.transformer = TfidfTransformer()

    def fit_transform(self, some_text: list[str]) -> list :
        matrix = super().fit_transform(some_text)
        return self.transformer.fit_transform(matrix)


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    transformer = TfidfTransformer()
    tf_idf = transformer.fit_transform(count_matrix)
    print(tf_idf)

    tf_idvectorizer = TfidfVectorizer()
    print(tf_idvectorizer.fit_transform(corpus))
    print(tf_idvectorizer.get_feature_names())




