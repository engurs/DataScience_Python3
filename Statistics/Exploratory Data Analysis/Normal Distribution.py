import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ECDF

michelson_speed_of_light = (pd.read_csv('michelson_speed_of_light.csv'))['velocity of light in air (km/s)']

# Compute mean and standard deviation
mean = np.mean(michelson_speed_of_light)
std = np.std(michelson_speed_of_light)

# Compute Normal Distribution
samples = np.random.normal(mean, std, size=10000)

# Compute ECDF
x, y = ECDF.ecdf(michelson_speed_of_light)

# Compute ECDF from normally distributed data
x_theor, y_theor = ECDF.ecdf(samples)

# Plot the ECDFs together
sns.set()

_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Speed of light (km/s)')
_ = plt.ylabel('CDF')

# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('ECDF of the data', 'Normally dist. theoretical data '))
plt.show()
