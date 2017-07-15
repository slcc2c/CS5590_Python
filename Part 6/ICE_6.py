import numpy as np
import matplotlib.pyplot as plt


data = np.array([[0.0,1.0],[1.0,3.0],[2.0,2.0],[3.0,5.0],[4.0,7.0],[5.0,8.0],[6.0,8.0],[7.0,9.0],[8.0,10.0],[9.0,12.0]])
means = []
for row in data.T:
    means.append(sum(row)/len(row))
SSxy = []
SSxx = []

for row in data.T:
    SSxy.append(0.0)
    SSxx.append(0.0)
    for i in row:
        SSxy[len(SSxy)-1] += i - means[len(SSxy)-1]
        SSxx[len(SSxx) - 1] += (i - means[len(SSxx) - 1]) ** 2
beta1 = (SSxy[0]*SSxy[1])/SSxx[0]
beta0 = means[1] - beta1*means[0]

x = np.linspace(0,9, 1000)
y = beta0 + (beta1 * x)


plt.plot(x,y)
plt.scatter(data.T[0],data.T[1])
plt.show()

