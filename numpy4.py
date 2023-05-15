import numpy as np
from scipy.stats import linregress

x = np.array([1,2,3,4,5])
y = np.array([2,4,5,6,7])

slope, intercept, r_value, p_value, std_err = linregress (x, y)
print(slope, intercept)