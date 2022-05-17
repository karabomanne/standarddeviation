IA = 100000 #Investment amount
pA = 0.05 #Probability of return is +50%
pB = 0.25 #Probability of return is +30%
prA = 0.5 #Probablereturn for pA
prB = 0.3 #Probable return for pB

erA = pA * prA * pB * prB + 0.4 * (pA+pA) + pB * (-pA-pA) + pA * (-prA)   #Expected return calculation

erB = pA * prA**2 * pB * prB**2 + 0.4 * (pA+pA)**2 + pB * (-pA-pA)**2 + pA * (-prA)**2   #Weighted return calculation

ep = [0.5, 0.3] #Estimated profit
epr = [0.05, 0.25] #Estimated probable return 

import numpy as np

std = np.sqrt(erB-erA**2) * 100
print ("the standard deviation of the annual return is {:0.2f}%". format(std))

import matplotlib.pyplot as plt
ep = list(range(2))
epr = list(range(2))
plt.figure (figsize = (12, 8)
plt.scatter(ep, epr, color = "b", markersize = 15)
plt.hines(y = 0, xmin = ep[0], xmax = ep[1], linestyle = "dashed")
plt.show()
