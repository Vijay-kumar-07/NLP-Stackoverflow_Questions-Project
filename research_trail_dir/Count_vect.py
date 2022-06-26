from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "apple ball cat dog",
    "elephant is huge",
    "I am so happy"
]

max_features = 100
ngrams = 3 # Trigram
vectorizer = CountVectorizer(max_features= max_features, ngram_range=(1,ngrams))
X = vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())