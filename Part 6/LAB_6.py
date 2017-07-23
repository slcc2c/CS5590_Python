import numpy as np
import matplotlib.pyplot as plt
#1)
data = np.loadtxt('ex2data1.txt',delimiter=",")
data = data[:,:2]


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

x = np.linspace(0,100,5)
y = beta0 + (beta1 * x)


plt.plot(x,y)
plt.scatter(data.T[0],data.T[1])
plt.show()


#2)
import numpy as np
import matplotlib.pyplot as plt
import random

def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def new_center(mu, cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    #for k in keys:
    #    newmu.append(np.mean(cluster[k],axis = 0))
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in temp1])
    temp2 = np.random.randint(N, size=K)
    newmu = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmu)
    itr = 0
    plot_cluster(oldmu,cluster,itr)
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster = cluster_content(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(newmu, cluster)
    plot_cluster(newmu, cluster, itr)
    return

def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

def init_graph(N, p1, p2):
    X = np.array([(random.uniform(p1,p2),random.uniform(p1,p2))for i in range(N)])
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    N = int(input('Enter the number of points.......'))
    K = int(input('Enter the number of Clusters.......'))
    print('Now Enter the bounds for choosing uniform value....\n')
    p1 = int(input('Enter the lower bound for points.......'))
    p2 = int(input('Enter the upper bound for points.......'))
    X = init_graph(N, p1, p2)
    #for x in X:
    #    plt.plot(x[0],x[1])
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    temp = Apply_Kmeans(X, K, N)


if __name__ == '__main__':
    Simulate_Clusters()

#3) Spectral clustering using Laplacian Matrices to develop similarity graphs and reduce the dimensionality of data before clustering