import matplotlib.pyplot as plt
from random import randint
import pandas as pd

n = 100000
cov_values = []

for i in range(n):

    vec_1 = [randint(0,100) for i in range(100)]
    vec_2 = [randint(0,100) for i in range(100)]

    data = pd.DataFrame({'X': vec_1, 'Y': vec_2})

    covariance_matrix = data.cov()
    cov_values.append(covariance_matrix.iloc[1, 0])

# print("Average Covariance: " + str(cov_tally/n))

plt.hist(cov_values, bins=100, density=True)
plt.title('Covariance Frequency Distribution')
plt.xlabel('Covariance')
plt.ylabel('Frequency')
plt.show()

'''
MC PMF for covariance of uniformly distributed integers seems to be roughly ~ normal to the eyeball
'''

# help(pd.DataFrame.cov)
