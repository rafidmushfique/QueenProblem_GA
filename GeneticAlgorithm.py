# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:54:49 2020

@author: RafiD
"""


import numpy as np
import pandas as pd
def fitness(population, n):
    rlist=[]
    m=len(population)
    for i in range(0,m):   
       cnt=0
       for j in range(0,n):
           cnt=cnt+atckpair(population[i],j)
       fitnessval=n*(n-1)
       fitnessval=fitnessval/2
       fitnessval=fitnessval-cnt
       rlist.append(fitnessval)
    return rlist
def atckpair(a,i):
    #print("here in atck")
    cnt=0
    cnt=cnt+horiatck(a,i)
    cnt=cnt+upvertiatck(a,i)
    cnt=cnt+lowvertiatck(a,i)
    return cnt
def upvertiatck(ar,ind):
    #print("here in up")
    cnt=0
    loc=0
    for i in range(0,8):
        if(i>ind):
            loc=loc+1
            if(ar[ind]+loc==8):
                break
            if(ar[ind]+loc==ar[i]):
                #print("here working")
                cnt=cnt+1
    return cnt
def lowvertiatck(ar,ind):
    #print("here in low")
    cnt=0
    loc=0
    for i in range(0,8):
        if(i>ind):
            loc=loc-1
            if(ar[ind]+loc==-1):
                break
            if(ar[ind]+loc==ar[i]):
                cnt=cnt+1
    return cnt
    
def horiatck(ar,ind):
    cnt=0
    loc=0
    for i in range(0,8):
        if(i>ind):
            if(ar[ind]==ar[i]):
                cnt=cnt+1       
    return cnt
def select(population, fit):
    data=pd.DataFrame(population, columns=["A", "B", "C", "D", "E", "F", "G", "H"])
    data2=pd.DataFrame(fit, columns=['fit'])
    data=pd.concat([data,data2],axis=1)
    data=data.sort_values(by=['fit'],ascending=False)
    selectind=np.random.randint(0, len(fit)/3)
    select=data.iloc[selectind:selectind+1,0:9]        
    os=[]
    for i in range(0,8):
     os.append(select.iat[0,i])
    return os

def crossover(x, y):
  cp = np.random.randint(1,n-1)
  # print(cp)
  # print(len(x))
  # print(len(y))
  child = []
  for i in range(0, 8):
      if(i<cp):
          child.append(x[i])
      else:
          child.append(y[i])     
  return child
 
def mutate(child):
  '''take input: a child
     mutates a random 
     gene into another random gene
     
     returns: mutated child'''
  randind=np.random.randint(0,n)
  randq=np.random.randint(0,n)
  child[randind]=randq
  randq=np.random.randint(0,n)
  child[randind]=randq

  return child
def intialPop(population,fit):
    data=pd.DataFrame(population, columns=["A", "B", "C", "D", "E", "F", "G", "H"])
    data2=pd.DataFrame(fit, columns=['fit'])
    data=pd.concat([data,data2],axis=1)
    data=data.sort_values(by=['fit'],ascending=False)
    z=[]
    for i in range (0,2):
        #print("here")
        os=[]
        select=data.iloc[i:i+1,0:8]
        for j in range(0, 8):
            os.append(select.iat[0,j])
        z.append(os)
    return z
    
def GA(population, n, mutation_threshold = 0.3,cnt = 0):
    cnt = cnt + 1
    fit = fitness(population, n)
    x = select(population,fit)
    y = select(population,fit)
    child = crossover(x,y)
    newthreshold = np.random.randint(0, 11)
    if (newthreshold < mutation_threshold*10):
        child = mutate(child)
    count = 0
    for j in range(0, n):
        #print("here")
        cnt = cnt + atckpair(child, j)
    osf = ((n * (n - 1))/2) - count
    child = np.array([child[:]])
    a = np.sort(fit)
    b = a [0]
    if(osf>b ):
        population = np.concatenate((population,child))
    return population
'''for 8 queen problem, n = 8'''
n = 8

'''start_population denotes how many individuals/chromosomes are there
  in the initial population n = 8'''
start_population = 10 

'''if you want you can set mutation_threshold to a higher value,
   to increase the chances of mutation'''
mutation_threshold = 0.3

'''creating the population with random integers between 0 to 7 inclusive
   for n = 8 queen problem'''
population = np.random.randint(0, n, (start_population, n))
population=np.array(population)
'''calling the GA function'''
print(GA(population, n, mutation_threshold))
