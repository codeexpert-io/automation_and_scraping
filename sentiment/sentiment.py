import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from tabulate import tabulate

#Instantiate model
tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

#scrape reviews from website
r = requests.get('https://www.yelp.com/biz/boxcar-bar-arcade-greensboro#reviews')
soup = BeautifulSoup(r.text,'html.parser')
regex = re.compile('.*comment.*')
results = soup.find_all('p',{'class':regex})
reviews = [result.text for result in results]

#print tabulated reviews
df = pd.DataFrame(np.array(reviews), columns=['review'])
print(tabulate(df.tail()))

#function to calculate sentiment
def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1

#concisely print index numbers with sentiment score
df['sentiment'] = df['review'].apply(lambda x: sentiment_score(x[:512]))
print(df['sentiment'])
