class CountVectorizer:
    def __init__(self):
        self.words = []
        self.matrix = []
        self.termfreq = []
        pass

    def fit_transform(self, some_text: list[str]) -> list:
        mat=[]
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

    if __name__ == '__main__':
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]
        vectorizer = CountVectorizer()
        count_matrix = vectorizer.fit_transform(corpus)
        print(vectorizer.get_feature_names())
        print(count_matrix)

    # def get_feature_names(self,corpus) -> list:
    # word_matrix = []
    # for sentences in self:
    # word_matrix.append(sentences.strip().split(' '))
    # word_matr = []
    # for i in word_matrix:
    # word_matr = word_matr + i
    # return list(set(word_matr))

    # def fit_transform(self,corpus) -> list:

    # for elements in corpus:
    # words = elements.lower().split()
    # mass=[]
    # for sent in self.get_feature_names(corpus):
    # num_words = words.count(sent)
    # mass.append(num_words)
    # fin.append(mass)
