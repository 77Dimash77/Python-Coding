# Задача 40: Работать с файлом california_housing_train.csv, 
# который находится в папке sample_data. Определить среднюю стоимость дома,
# где кол-во людей от 0 до 500 (population).

import pandas as pd

df = pd.read_csv('california_housing_train.csv', sep=',', encoding='cp1251')

filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]

mean_house_value = filtered_df['median_house_value'].mean()

print("Средняя стоимость дома для количества людей от 0 до 500:", mean_house_value)
