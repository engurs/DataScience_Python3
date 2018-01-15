import pandas as pd
import matplotlib.pyplot as plt


df_swing = pd.read_csv('2008_swing_states.csv')

_ = plt.plot(df_swing['total_votes']/1000, df_swing['dem_share'], marker='.', linestyle='none')
# Set margins
_ = plt.margins(0.02)

# Label the axes
_ = plt.xlabel('Total votes (thousands)')
_ = plt.ylabel('percent of vote for Obama')

# Show the result
plt.show()