

#### Assignment 1 - Scraper Script
#### Team members: Alex Kim, Bolun Zhang, Chu Nie, Davis Gill

# import packages

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


headers = {'Accept-Languages':"en-US,en;q=0.5"}
date = []
dateTime = []
message = []
old_pages = np.arange(1,110,1)
for page in old_pages:

    print(page)

    page = requests.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p'+str(page))
    soup = BeautifulSoup(page.text,'html.parser')

    comment_data = soup.findAll('div',attrs = {'class':'Comment'})

    sleep(randint(2,8))

    for c in comment_data:

        # Date and DateTime
        d = c.time.attrs['title'] # date
        dt = c.time.attrs['datetime'] # dateTime
        date.append(d)
        dateTime.append(dt)

        # Comment Body Paragraph
        comment = c.find('div', class_ = 'Message userContent').text
        message.append(comment)
        

old_luxury_sedan_comments = pd.DataFrame({'date':date, 'dateTime':dateTime, 'message': message})
old_luxury_sedan_comments = old_luxury_sedan_comments.drop_duplicates(['message'])
old_luxury_sedan_comments.reset_index(drop = True)

old_luxury_sedan_comments.to_csv('old_luxury_sedan_comments.csv')



date = []
dateTime = []
message = []
new_pages = np.arange(435,325,-1)
for page in new_pages:

    print(page)

    page = requests.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p'+str(page))
    soup = BeautifulSoup(page.text,'html.parser')

    comment_data = soup.findAll('div',attrs = {'class':'Comment'})

    sleep(randint(2,8))

    for c in comment_data:

        # Date and DateTime
        d = c.time.attrs['title'] # date
        dt = c.time.attrs['datetime'] # dateTime
        date.append(d)
        dateTime.append(dt)

        # Comment Body Paragraph
        comment = c.find('div', class_ = 'Message userContent').text
        message.append(comment)
        

new_luxury_sedan_comments = pd.DataFrame({'date':date, 'dateTime':dateTime, 'message': message})
new_luxury_sedan_comments = new_luxury_sedan_comments.drop_duplicates(['message'])
new_luxury_sedan_comments.reset_index(drop = True)

new_luxury_sedan_comments.to_csv('new_luxury_sedan_comments.csv')