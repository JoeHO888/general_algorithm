import numpy as np
import matplotlib.pyplot as plt
generation_size=100
pop_size=500
cities_size=20
mutation_rate=0.02
crossover_rate=0.2
map_size=21

d={}

for x in range(0,cities_size):
        d[int("{}".format(x))]=np.random.randint(map_size,size=(2,1))

x=np.array([d[e][0] for e in d])
y=np.array([d[e][1] for e in d])

def mutate(children):
  for e in children:
    for i in range(cities_size):
      if np.random.uniform(0,1,1)<mutation_rate:
        a=e[i]
        s=np.random.randint(cities_size,size=1)
        e[i]=e[s]
        e[s]=a
  return children

def fitness(pop):
  fitness=np.zeros(pop_size)
  for j in range(pop_size):
    fitness[j]=np.exp(1.0/np.sum([np.linalg.norm(d[pop[j,i]]-d[pop[j,i+1]]) for i in range(cities_size-1)]))
  return fitness


def select(pop):
  index=np.random.choice(pop_size, pop_size, replace=True,p=fitness(pop)/fitness(pop).sum()) 
  return np.array([pop[i] for i in index]) 

def crossover(dad,pop):
  for i in range(dad.shape[0]):
    if np.random.uniform(0,1,1)<crossover_rate:
      i_ = np.random.randint(0, cities_size, size=1) 
      cross_points = np.random.randint(0, 2, cities_size).astype(np.bool) #ok
      keep_city=dad[i,~cross_points]
      swap_city = pop[i_, np.isin(pop[i_].ravel(), keep_city, invert=True)]
      dad[i,:] = np.concatenate((keep_city, swap_city))
  return dad
        
      
g=np.array([np.random.choice(cities_size,cities_size,replace=False) for i in range(pop_size)])

for i in range(generation_size):
  print("gen: "+str(i))
  hor=np.array([d[e][0] for e in g[np.argmax(fitness(g))]])
  ver=np.array([d[e][1] for e in g[np.argmax(fitness(g))]])
  plt.figure(figsize=(20,10))
  plt.plot(x, y,"ro",ms=20)
  plt.plot(hor, ver,linewidth=3)
  plt.show() 
  parent=select(g)
  children=crossover(parent,g)
  g=mutate(children)
