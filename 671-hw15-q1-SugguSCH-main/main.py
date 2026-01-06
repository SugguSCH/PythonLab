# YOUR CODE HERE
import pandas as pandata
dataframe = pandata.read_csv('data.csv')
words = input()
output = dataframe['text'].str.count(words).sum()
print(output)