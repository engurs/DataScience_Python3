import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_swing = pd.read_csv('2008_swing_states.csv')
sns.set()
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')

plt.show()
