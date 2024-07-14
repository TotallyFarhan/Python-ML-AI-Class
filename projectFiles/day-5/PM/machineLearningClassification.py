import numpy as np
import pandas as pd
 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
 
dataframe = pd.read_csv("gamespot_game_reviews.csv")

reviews_dataframe = dataframe[['tagline', 'classifier']]

print(reviews_dataframe)

tagline_list = reviews_dataframe['tagline'].tolist()
count_vect = CountVectorizer()
words_train_counts = count_vect.fit_transform(tagline_list)
 
tfidf = TfidfTransformer()
words_train_tfidf = tfidf.fit_transform(words_train_counts)
 
split_results = train_test_split(words_train_tfidf, np.array(reviews_dataframe['classifier']), test_size=0.3)
train_words = split_results[0]
test_words = split_results[1]
train_reviews = split_results[2]
test_reviews = split_results[3]

classification_model = MultinomialNB().fit(train_words, train_reviews)
testing_score = classification_model.predict(test_words)

number_right = 0
for i in range(len(testing_score)):
    if testing_score[i] == test_reviews[i]:
        number_right +=1
 
print("Accuracy for tagline classify: %.2f%%" % ((number_right/float(len(test_reviews)) * 100)))
        
