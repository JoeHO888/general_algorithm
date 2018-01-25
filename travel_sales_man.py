import numpy as np

generation_size=10
pop_size=10
cities_size=10
mutation_rate=0.001
crossover_rate=0.8
map_size=11

d={}

for x in range(0,cities_size):
        d[int("{}".format(x))]=np.random.randint(map_size,size=(2,1))


def mutate(children):
  for e in children:
    for i in range(10):
      if np.random.uniform(0,1,1)<mutation_rate:
        a=e[i]
        s=np.random.randint(10,size=1)
        e[i]=e[s]
        e[s]=a
  return children

def fitness(pop):
  fitness=np.zeros((1,pop_size))
  for j in range(pop_size):
    fitness[0,j]=np.sum([np.linalg.norm(d[pop[j,i]]-d[pop[j,i+1]]) for i in range(cities_size-1)])
  return fitness


def select(pop):
  index=np.random.choice(pop_size, pop_size//2, replace=False,p=fitness(pop)/fitness(pop).sum()) 
  return np.array([pop[i] for i in index]) 

def crossover(parent):
  parent_copy=parent
  for i in range(parent.shape[0]):
    if np.random.uniform(0,1,1)<crossover_rate:
      








pop=np.array([np.random.choice(cities_size,cities_size,replace=False) for i in range(pop_size)])








        
  

