import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_swing = pd.read_csv('2008_swing_states.csv')
sns.set()
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('number of counties')

plt.show()
