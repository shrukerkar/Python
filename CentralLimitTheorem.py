import math
import random
from collections import Counter
import matplotlib.pyplot as plt


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
