#### Task B

import pandas as pd
import numpy as np
import nltk
import re

from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer


data = pd.read_csv('old_luxury_sedan_comments.csv')
car_info = pd.read_csv('car_models_and_brands.csv')

tokenizer = TreebankWordTokenizer()
words_unique = []
modelList = car_info.drop_duplicates()['Model'].to_list()
brandList = car_info.drop_duplicates()['Brand'].to_list()


for i in range(len(data)):
    
    temp = set() 
    m = data['message'][i]
    tokens = tokenizer.tokenize(m)

    for t in tokens: 
        t = t.lower()
        if t in modelList:
            n = modelList.index(t)
            t = brandList[n]
            temp.add(t)
        else:
            temp.add(t)
        
    for x in temp:
        x = str(x)
        words_unique.append(x)


words_unique_english = pd.Series(words_unique).value_counts().to_frame().reset_index()
words_unique_english.rename(columns = {'index':'word',0:'count'},inplace = True)
words_unique_english= words_unique_english[words_unique_english['word'].apply(lambda x: x.isalpha())]

stopWords = stopwords.words('english')
df_clean = words_unique_english[words_unique_english['word'].isin(stopWords)==False] # without stopWords
car_brand_count = df_clean[df_clean['word'].isin(brandList)].sort_values(['count'], ascending = False

car_brand_count.to_csv('car_brand_frequency.csv', index = False)