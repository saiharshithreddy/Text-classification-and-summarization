import os
import pandas as pd
categories = os.listdir('./data/')

categories.remove('us')
categories.remove('health')
dictionary = {'category' : [], 'content': []}
content = []
category = []
for c in categories:
    files = os.listdir('./data/'+c)
    for f in files:
       
        with open('./data/'+c +'/'+f, 'r') as text_file:
            data = text_file.readlines()
            
            content.append(data[1])
            category.append(data[-1])
            
    

dictionary['category'] = category
dictionary['content'] = content
df = pd.DataFrame(dictionary)

df.to_csv('news_data.csv')