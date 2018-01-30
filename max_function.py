import matplotlib.pyplot as plt
import numpy as np

mutation=0.01
crossover_rate=0.8
pop_size=100
generation=100
DNA_length=10
X_BOUND=[0,5]

def F(array):
  return 2*np.sin(array)+np.cos(array)

def fitness(pop):
  return F(pop)+4
  
def mutate(DNA):
  for e in DNA:
    for i in range(10):
      if np.random.uniform(0,1,1)<mutation:
        e[i] = 0 if e[i] ==1 else 1
  return DNA
        
def crossover(dad,pop): 
    for i in range(pop_size):
        if np.random.uniform(0,1,1)<crossover_rate:
            crosspoint=np.random.randint(0,DNA_length,size=1)[0]
            i=np.random.randint(0,pop_size,size=1)[0]
            dad[i,crosspoint:]=pop[i,crosspoint:][np.newaxis,:]
    return dad

def select(DNA):
  index=np.random.choice(pop_size, pop_size, replace=True,p=fitness(translateDNA(DNA))/fitness(translateDNA(DNA)).sum()) #problematic
  return np.array([DNA[i] for i in index]) 

def translateDNA(pop):
    return pop.dot(2 ** np.arange(DNA_length)[::-1]) / float(2**DNA_length-1) * X_BOUND[1]
    
DNA = np.random.randint(2, size=(pop_size, DNA_length))
x = np.linspace(*X_BOUND, 200)

for j in range(generation):
  pop=translateDNA(DNA) #pop.shape=(500,)
  plt.plot(x, F(x))
  plt.plot(pop,F(pop),"ro")
  plt.show()
  parents=select(DNA)
  child=crossover(parents,DNA)
  DNA=mutate(child)
