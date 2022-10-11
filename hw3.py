# from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]


class CountVectorizer:

    def get_feature_names(self) -> list:
        word_matrix = []
        for sentences in self:
            word_matrix.append(sentences.strip().split(' '))
        word_matr = []
        for i in word_matrix:
            word_matr = word_matr + i
        return list(set(word_matr))

    def fit_transform(self) -> list:

        for elements in self:
            words = (elements.lower()).split()
            mass=[]
            for sent in get_feature_names(self):
                num_words = words.count(sent)
                mass.append(num_words)
            fin.append(mass)