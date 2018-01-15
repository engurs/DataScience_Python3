import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_all_states = pd.read_csv('2008_swing_states.csv')

_ = sns.boxplot(x='east_west', y='dem_share', data=df_all_states)
_ = plt.xlabel('region')
_ = plt.ylabel('percent of vote for Obama')

plt.show()
