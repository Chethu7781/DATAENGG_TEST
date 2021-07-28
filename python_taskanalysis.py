import pandas as pd
from pandas import DataFrame
from pandas import json_normalize
import numpy as np

#DataFrame can be made through cursor and list(cursor) 
data = list(cursor)
df = pd.DataFrame(data)

unique_country = set()

for i in df['Country']:
    if i not in unique_country:
        unique_country.add(i)

print(unique_country)  #for knowing all the unique countries


#for sample flat file for INDIA Vaccinated people 
df1 = df[df['Country']=="IND"]
#so that we can easily find the people w.r.t country users and the data can be easily uploaded into database. 
