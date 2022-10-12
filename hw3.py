corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]


class CountVectorizer:
    def __init__(self,corpus):


    def get_feature_names(self,corpus) -> list:
        word_matrix = []
        for sentences in self:
            word_matrix.append(sentences.strip().split(' '))
        word_matr = []
        for i in word_matrix:
            word_matr = word_matr + i
        return list(set(word_matr))

    def fit_transform(self,corpus) -> list:

        for elements in corpus:
            words = elements.lower().split()
            mass=[]
            for sent in self.get_feature_names(corpus):
                num_words = words.count(sent)
                mass.append(num_words)
            fin.append(mass)

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform
print(count_matrix)