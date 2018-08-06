import math
import random
from collections import Counter

import matplotlib.pyplot as plt

def normal_pdf(x,mu=0,sigma=1):
    sqrt_of_twopi= math.sqrt(2*math.pi)
    return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_of_twopi * sigma))
xs=[ x/10.0 for x in range(-50,50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2)for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,mu=-1)for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("various normal pdf's")
plt.show()


def normal_cdf(x,mu=0,sigma=1):
    return (1+math.erf(x-mu)/math.sqrt(2)*sigma)
xs=[ x/10.0 for x in range(-50,50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2)for x in xs],'--',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,mu=-1)for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend(loc=4)
plt.title("various normal cdf's")
plt.show()
def burnoulli_trail(n,p):
    return 1 if random.random()< p else 0
def binomial(n,p):
    return sum(burnoulli_trail(p) for _ in range(n))
def make_hist(p,n,num_points):
    data=[binomial(n,p) for _ in range (num_points)]
    histogram=Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()],[v / num_points for v in histogram.values()],0.8,color='0.75')
    mu=n*p
    sigma=math.sqrt(n*p(1-p))
    xs= range (min(data),max(data)+1)
    ys=[normal_cdf(i+0.5,mu,sigma)-normal_cdf(i-0.5,mu,sigma)]
    plt.plot(xs,ys)
    plt.title('Binomial distribution vs normal distribution')
    plt.show()
def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.0001):
    if mu!=0 and sigma!=1:
        return mu+ sigma*inverse_normal_cdf(p,tolerance=tolerance)
    low_z,low_p=-10,0
    hi_z,hi_p=101
    while hi_z - low_z>tolerance:
        mid_z=(low_z+hi_z)/2
        mid_p=normal_cdf(mid_z)
    if mid_p > p:
        low_z,low_p=mid_z,mid_p
    elif mid_p < p:
        hi_z,hi_p=mid_z,mid_p
    else:
        pass     #break
    return mid_z