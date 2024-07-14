import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer

df = pd.read_csv("gamespot_game_reviews.csv")

reviews_df = df[['tagline', 'classifier']]
print(reviews_df)


tagline_list = reviews_df['tagline'].tolist()
count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(tagline_list)

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
print(x_train_tfidf.shape)
print(x_train_tfidf.data)


split_results = train_test_split(x_train_tfidf, np.array(reviews_df['classifier']), test_size=0.3)
train_x = split_results[0]
test_x = split_results[1]
train_y = split_results[2]
test_y = split_results[3]

classification_model = MultinomialNB().fit(train_x, train_y)
y_score = classification_model.predict(test_x)

print(y_score)

number_right = 0
for i in range(len(y_score)):
    if y_score[i] == test_y[i]:
        number_right +=1

print("Accuracy for tagline classify: %.2f%%" % ((number_right/float(len(test_y)) * 100)))
