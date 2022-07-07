import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

car = pd.read_csv('D:\Code_Ground\datatitanic\car.csv')
print(car)

# print(car.head(5))
# print(car.describe()) #display the stats about the data
# print(car.info()) # display the basic info about datatype
# print(car.isnull().sum()) #to check null values

# Dropping irrelevant column

car = car.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
# print(car.head(5))

# Renaming the columcar

car = car.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
# print(car.head(5))

# # Dropping the duplicate rows

# print(car.shape)

duplicate_rows_car = car[car.duplicated()]
# print("number of duplicate rows: ", duplicate_rows_car.shape)

# print(car.count())

car = car.drop_duplicates()
# print(car.head(5))
# print(car.count())

# # Dropping the missing or null values

# print(car.isnull().sum())

# car = car.dropna()    # Dropping the missing values.
# print(car.count())

# print(car.isnull().sum())   # After dropping the value


# # Detecting Outlier

# sns.boxplot(x=car['Price'])
# plt.show()

# sns.boxplot(x=car['HP'])
# plt.show()

# sns.boxplot(x=car['Cylinders'])
# plt.show()

Q1 = car.quantile(0.25)
Q3 = car.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# # Plot different features against one another

# car.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
# plt.title("Number of cars by make")
# plt.ylabel('Number of cars')
# plt.xlabel('Make')
# plt.show()

corr = car.corr()
# print(corr)

# fig, ax = plt.subplots(figsize=(3,4))
# sns.heatmap(corr, annot=True, ax = ax)
# plt.show()

# fig, ax = plt.subplots(figsize=(10,6))
# ax.scatter(car['HP'], car['Price'])
# ax.set_xlabel('HP')
# ax.set_ylabel('Price')
# plt.show()





