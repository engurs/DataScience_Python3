import ECDF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_swing = pd.read_csv('2008_swing_states.csv')

# Specify array of percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles for first 100
ptiles_dem_share = np.percentile((df_swing['dem_share'])[:100], percentiles)

# Compute ECDF for first 100
x, y = ECDF.ecdf((df_swing['dem_share'])[:100])


# Plot the ECDF
_ = plt.plot(x, y, '.')
plt.margins(0.02)
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_dem_share, percentiles/100, marker='D', color='red', linestyle='none')

# Show the plot
plt.show()
