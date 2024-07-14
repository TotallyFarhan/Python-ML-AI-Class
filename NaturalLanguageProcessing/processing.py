import requests
from bs4 import BeautifulSoup
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

nltk.download()

nintendo_wiki = 'https://en.wikipedia.org/wiki/Nintendo'
page = requests.get(nintendo_wiki)

soup = BeautifulSoup(page.text, 'html.parser')
text = soup.get_text(separator = ' ', strip = True)

clean_text = text.lower()

table = str.maketrans("", "", string.punctuation)
clean_text = clean_text.translate(table)

words = clean_text.split()

clean_words = []
#for token in words:
#    if token not in stopwords.words('english'):
#        clean_words.append(token)

#freq = nltk.FreqDist(clean_words)

#freq.plot(20, title = "Frequency Distribution")

sentences = sent_tokenize(text)

sentence_words = sentences[8].split()
first_sentence = ' '.join(sentence_words[-18:])

nltk_words = word_tokenize(text)

print(nltk_words)