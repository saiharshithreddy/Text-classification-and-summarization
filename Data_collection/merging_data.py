import os
import pandas as pd
path = './final_data'
from os import listdir
from os.path import isfile, join

files = [f for f in listdir(path) if isfile(join(path, f))]

for i, filename in enumerate(files):
    
   globals()['df%s' % i] = pd.read_pickle(path+'/'+filename)
    
df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23])
df.to_pickle('news_data.pickle')
