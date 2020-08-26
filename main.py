import pandas as pd
import numpy as np
import re
data = pd.read_csv("Ingredients.csv")
df=pd.DataFrame(data=data)
import __init__
import utils
import en
import test_new_feature
from en import parse

print(parse("Roasted scrapped egg"))
a=[]
b=[]
c=[]
for i in range(len(df)):
   a.append(parse(df["Ingredient Name"][i]))
   b.append(a[i]['name'].split())
   c.append(b[i][0])
   print(c)
   
data=list(zip(df["Ingredient Name"],c))
df=pd.DataFrame(data=data)
df.to_csv('new.csv',index=False,encoding='utf-8')
