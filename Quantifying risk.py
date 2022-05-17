IA = 100000 #Investment amount
pA = 0.05 #Probability return is +50%
pB = 0.25 #Probability return is +30%
prA = 0.5 #Probable return for pA
prB = 0.3 #Probable return for pB

erA = pA * prA * pB * prB + 0.4 * (pA+pA) + pB * (-pA-pA) + pA * (-prA)   #Expected return calculation

erB = pA * prA**2 * pB * prB**2 + 0.4 * (pA+pA)**2 + pB * (-pA-pA)**2 + pA * (-prA)**2   #Weighted return calculation
cf = [0.05, 0.50, 0.25, 0.3]

import numpy as np

for std in (len(cf))
std = np.sqrt(erB-erA**2)
print ("the standard deviation of the annual return is {}%". format(std))

import matplotlib.pyplot as plt

x_axis = list(range(std))
plt.scatter(x_axis, cf)
plt.show()
 