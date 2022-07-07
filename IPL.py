import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

ipl = pd.read_csv('D:\Code_Ground\datatitanic\IPL.csv')

#import file from filepath

print(ipl)

# print(ipl.head(5))

# print(ipl.describe()) #display the stats about the data

# print(ipl.info()) # display the basic info about datatype

# print(ipl.isnull().sum()) #to check null values

# print(ipl['season'].unique())

# sns.countplot(x='season', data=ipl)

# plt.show()   # Which season had most number of matches? 2013

# sns.countplot(y='winner', data = ipl)

# plt.show()

# data = ipl.winner.value_counts() 

# sns.barplot(y = data.index, x = data, orient='h')

# plt.show()   # the most successful ipl team


# top_players = ipl.player_of_match.value_counts()[:10]
# #sns.barplot(x="day", y="total_bill", data=tips)
# fig, ax = plt.subplots()
# ax.set_ylim([0,20])
# ax.set_ylabel("Count")
# ax.set_title("Top player of the match Winners")
# #top_players.plot.bar()
# sns.barplot(x = top_players.index, y = top_players, orient='v'); #palette="Blues");
# plt.show()   # top player of the match winner

# Has Toss-winning helped in Match-winning?

# Toss = ipl['toss_winner'] == ipl['winner']

# # print(Toss.groupby(Toss).size())

# sns.countplot(ipl['toss_winner'] == ipl['winner'])
# sns.countplot(Toss)
# plt.show()
