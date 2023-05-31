import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

encoder = OneHotEncoder()
data_encoded = encoder.fit_transform(data[['whoAmI']]).toarray()

df_encoded = pd.DataFrame(data_encoded, columns=encoder.categories_[0])

df_encoded.head()
print(df_encoded)