# YOUR CODE HERE
import pandas as pd
df = pd.read_csv('data.csv')

male_more_40 = df[(df['Sex'] == 'male') & (df['Age'] > 40)]
class1male = len(male_more_40[male_more_40["Pclass"] == 1].value_counts())
class2male = len(male_more_40[male_more_40["Pclass"] == 2].value_counts())
class3male = len(male_more_40[male_more_40["Pclass"] == 3].value_counts())

female_more_40 = df[(df['Sex'] == 'female') & (df['Age'] > 40)]
class1female = len(female_more_40[female_more_40["Pclass"] == 1].value_counts())
class2female = len(female_more_40[female_more_40["Pclass"] == 2].value_counts())
class3female = len(female_more_40[female_more_40["Pclass"] == 3].value_counts())

print("male (age>40)")
print(f"Pclass 1: {class1male}")
print(f"Pclass 2: {class2male}")
print(f"Pclass 3: {class3male}")
print("female (age>40)")
print(f"Pclass 1: {class1female}")
print(f"Pclass 2: {class2female}")
print(f"Pclass 3: {class3female}")
