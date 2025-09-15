import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')
new_titanic = pd.DataFrame(titanic, columns=['pclass', 'sex', 'age', 'fare', 'who', 'alive'])

titanic_pivoted = titanic.pivot_table(index='pclass', columns='sex', values='survived', aggfunc='size')
sns.heatmap(titanic_pivoted, cmap=sns.light_palette('crimson', as_cmap=True), annot=True, fmt='d')

print(titanic_pivoted)
plt.show()