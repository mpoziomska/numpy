import numpy as np

tab = np.loadtxt('data/iris.csv', delimiter=',', skiprows=1, usecols=(0,1,2,3))

print(tab.shape)

mean_tab = np.mean(tab, axis=0)

median_tab = np.median(tab, axis=0)

std_tab = np.std(tab, axis=0)

print(f'Means: {mean_tab}')
print(f'Medians: {median_tab}')
print(f'Std: {std_tab}')