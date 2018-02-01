import matplotlib.pyplot as plt
import numpy as np

mutation=0.01
crossover_rate=0.8
pop_size=100
generation=100
DNA_length=10
X_BOUND=[0,5]
compare_times=10

def F(x):
    return 2*np.sin(x)+np.cos(x)

def fitness(pop):
    return F(pop)+4
  
def mutate(DNA):
    for i in range(DNA_length):
        if np.random.uniform(0,1,1)<mutation:
            DNA[i] = 0 if DNA[i] ==1 else 1
    return DNA
        
def crossover(DNA):
    for i in range(compare_times):
        if np.random.uniform(0,1,1)<crossover_rate:
            i=np.random.randint(0,pop_size,size=1)[0]
            j=np.random.randint(0,pop_size,size=1)[0]
            if fitness(translateDNA(DNA)[i])>fitness(translateDNA(DNA)[j]):
                winner=DNA[i]
                loser=DNA[j]
            else:
                winner=DNA[j]
                loser=DNA[i]
            crosspoint=np.random.randint(0,DNA_length,size=1)[0]
            loser[crosspoint:]=winner[crosspoint:]
            loser=mutate(loser)
    return DNA

def translateDNA(pop):
    return pop.dot(2 ** np.arange(DNA_length)[::-1]) / float(2**DNA_length-1) * X_BOUND[1]
    
DNA = np.random.randint(2, size=(pop_size, DNA_length))
x = np.linspace(*X_BOUND, 200)

for j in range(generation):
    pop=translateDNA(DNA) #pop.shape=(500,)
    plt.plot(x, F(x))
    plt.plot(pop,F(pop),"ro")
    plt.show()
    DNA=crossover(DNA)
