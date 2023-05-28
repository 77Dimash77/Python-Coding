# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd

df = pd.read_csv('california_housing_train.csv', sep=',', encoding='cp1251')

min_population = df['population'].min()

min_population_data = df[df['population'] == min_population]

max_households = min_population_data['households'].max()

print("Максимальное количество households в зоне минимального значения population:", max_households)
