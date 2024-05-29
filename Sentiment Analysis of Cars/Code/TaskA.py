# Task A
# Team Members: Alex Kim, Bolun Zhang, Chu Nie, Davis Gill
import pandas as pd
import numpy as np
import nltk
import re
import matplotlib.pyplot as plt
from nltk.tokenize import TreebankWordTokenizer

data = pd.read_csv('old_luxury_sedan_comments.csv')

tokenizer = TreebankWordTokenizer()
word_book = set()
words = []

for i in range(len(data)):
    
    m = data['message'][i]
    tokens = tokenizer.tokenize(m)
    for t in tokens:
        word_book.add(t.lower())
        words.append(t.lower())


counts = [(w, words.count(w)) for w in word_book]

def takeSecond(elem):
    return elem[1]

counts.sort(key = takeSecond,reverse = True)

w, c = zip(*counts)

top_100_words = w[0:100]
top_100_words_freq = c[0:100]

rank = np.arange(1,101)

# Theoretical Zipf's Law
constant = 1*c[0] # constant = rank * frequency
zipf_pred = constant / rank

# Plot
plt.figure(figsize = (10,7))
plt.plot(rank,zipf_pred, marker = '.',label = "Zipf's Law Theoretical Prediction")
plt.plot(rank,top_100_words_freq, marker = '.',label = "Reality")
plt.xlabel('rank')
plt.ylabel('frequency')
plt.title("Most Common 100 Words in Reality vs. in Zipf's Law Theoretical Prediction")
plt.legend()

plt.savefig('mostCommon100Words.svg',format = 'svg')


# Plot Log
plt.figure(figsize = (10,7))
plt.plot(rank,zipf_pred, marker = '.',label = "Zipf's Law Theoretical Prediction")
plt.plot(rank,top_100_words_freq, marker = '.',label = "Reality")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('rank')
plt.ylabel('frequency')
plt.title("Most Common 100 Words in Reality vs. in Zipf's Law Theoretical Prediction (log)")
plt.legend()

plt.savefig('mostCommon100Words_log.svg',format = 'svg')