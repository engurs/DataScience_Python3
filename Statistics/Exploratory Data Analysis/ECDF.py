import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ECDF => Empirical cumulative distribution functions


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points
    n = len(data)

    # x-data for the ECDF
    x = np.sort(data)

    # y-data for the ECDF
    y = np.arange(1, n+1) / n

    return x, y


df_swing = pd.read_csv('2008_swing_states.csv')
# Compute ECDF
x, y = ecdf(df_swing['dem_share'])

# Plot ECDF
_ = plt.plot(x, y,  marker='.', linestyle='none')

# Keeps data off plot edges
_ = plt.margins(0.02)

# Annotate the plot
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
