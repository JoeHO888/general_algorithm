import numpy as np

generation_size=100
pop_size=100
cities_size=4
mutation_rate=0.1
crossover_rate=0.8
map_size=11

d={}

for x in range(0,cities_size):
        d[int("{}".format(x))]=np.random.randint(map_size,size=(2,1))

print(d)

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
  return 100-fitness


def select(pop):
  index=np.random.choice(pop_size, pop_size//2, replace=False,p=fitness(pop)/fitness(pop).sum()) 
  return np.array([pop[i] for i in index]) 

def crossover(dad,mom):
  for i in range(dad.shape[0]):
    if np.random.uniform(0,1,1)<crossover_rate:
      suffix=mom[i,cities_size//2:]
      for e in suffix:
        if e in dad[i,:cities_size//2]:
          candidates=set(dad[i,cities_size//2:]) - set(suffix)
          suffix[suffix == e] = np.random.choice(np.array(list(candidates)),1)
      dad[i]=np.hstack((dad[i,:cities_size//2],suffix))
  return dad

        
      
pop=np.array([np.random.choice(cities_size,cities_size,replace=False) for i in range(pop_size)])


for i in range(generation_size):
  print(max(fitness(pop)))
  dad=select(pop)
  mom=select(pop)
  children_1=crossover(dad,mom)
  children_2=crossover(dad,mom)
  children=np.vstack((children_1,children_2))
  pop=mutate(children)


#graph is needed

        
  

