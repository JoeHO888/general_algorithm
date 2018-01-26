import numpy as np
import matplotlib.pyplot as plt
generation_size=100
pop_size=100
cities_size=10
mutation_rate=0.02
crossover_rate=0.8
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
    fitness[j]=np.sum([np.linalg.norm(d[pop[j,i]]-d[pop[j,i+1]]) for i in range(cities_size-1)])
  return 1000-fitness


def select(pop):
  index=np.random.choice(pop_size, pop_size//2, replace=False,p=fitness(pop)/fitness(pop).sum()) 
  return np.array([pop[i] for i in index]) 

def crossover(dad,mom):
  for i in range(dad.shape[0]):
    if np.random.uniform(0,1,1)<crossover_rate:
      crossover_point=np.random.randint(0,cities_size,size=1)[0] #ok
      suffix=mom[i,crossover_point:]
      for e in suffix:
        if e in dad[i,:crossover_point]:
          candidates=set(dad[i,crossover_point:]) - set(suffix)
          suffix[suffix == e] = np.random.choice(np.array(list(candidates)),1)
      dad[i]=np.hstack((dad[i,:crossover_point],suffix))
  return dad
        
      
g=np.array([np.random.choice(cities_size,cities_size,replace=False) for i in range(pop_size)])

for i in range(generation_size):
  print("gen: "+str(i))
  hor=np.array([d[e][0] for e in pop[np.argmin(fitness(pop))]])
  ver=np.array([d[e][1] for e in pop[np.argmin(fitness(pop))]])
  plt.figure(figsize=(20,10))
  plt.plot(x, y,"ro",ms=20)
  plt.plot(hor, ver,linewidth=3)
  plt.show() 
  parent1=select(g)
  parent2=select(g)
  parent3=select(g)
  parent4=select(g)
  child_1=crossover(parent1,parent3)
  child_2=crossover(parent2,parent4)
  new_g=np.vstack((child_1,child_2))
  g=mutate(new_g)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
