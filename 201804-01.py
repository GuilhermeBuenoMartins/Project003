import random
import math
import numpy

class Points():
    def _init_(self):
        self.x = []
        self.y = []



def f(p, s):
    sum = 0.0 #Result of Sum of Euclidean distance
    for i in range(len(s)-1):
         sum += math.sqrt(math.pow(p.x[s[i]]-p.x[s[i+1]],2)+math.pow(p.y[s[i]]-p.y[s[i+1]],2))
    return sum
    

def solution(n):
    s = [0]
    s += random.sample(range(1,n-1), n-2)
    s.append(n-1)
    return s


def simulatedAnnealing():
    n = int(input('Define the number of points: '))
    p = Points()
    i=0
    p.x=[float(input('Point x'+str(i)+': '))]
    p.y=[float(input('Point y'+str(i)+': '))]
    while(i+1<n):
        p.x.append(float(input('Point x'+str(i+1)+': ')))
        p.y.append(float(input('Point y'+str(i+1)+': ')))
        i+=1

    print('\n\n\n')
    s0=[]
    s1=[]
    s=[]
    s0 = solution(n) #First Solution
    s = s0 #Best Found Solution
    IterT = 0 #Interation Number in Temperature T
    T = n #Current Temperature
    sAMax = math.pow(n,2)

    while(T > 0.0001):
        while(IterT <sAMax):
            IterT +=1
            s1=solution(n)#Generate an other solution
            delta = f(p, s1)-f(p, s0)
            if (delta<0):
                s0 = s1.copy()
                if(f(p, s1)<f(p, s)):
                    s = s1.copy()
            else:
                #Take x between 0 and 1
                x = 0.920
                if(x < numpy.exp(-delta/T)): #Probability of to be current state 
                    s0 = s1.copy()        
        T = T * 0.988
        Iter = 0
    return s


print(simulatedAnnealing())

