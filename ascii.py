import numpy as np

length=np.random.randint(1,10,size=1)[0] # 10 is max length
crossover_rate=0.8
mutation_rate=0.01
generation=200
population_size=500

target=np.random.randint(33,127,size=length)



def fitness(member):
    return length-np.count_nonzero(member-target)

def select(pop):
    probability=np.array([fitness(e) for e in pop])
    index=np.random.choice(population_size, population_size, replace=True,p=probability/probability.sum())
    return [probability,np.array([pop[i] for i in index])]

def crossover(parent):
    for e in parent:
        if  np.random.uniform(0,1,1)<crossover_rate:
            crosspoint=np.random.randint(0,length,size=1)[0]
            i=np.random.randint(0,population_size,size=1)[0]
            e[crosspoint:]=population[i,crosspoint:][np.newaxis,:]
    return parent

def mutate(pop):
    for e in pop:
        for i in range(len(e)):
            if np.random.uniform(0,1,1)<mutation_rate:
                e[i]=np.random.randint(33,127,size=1)
    return pop

    
print("target: "+"".join([chr(e) for e in target]))

population=np.random.randint(33,127,size=(population_size,length))

for i in range(generation):
    prob=select(population)[0]
    dad=np.array(select(population)[1])
    print("generation: "+str(i+1))
    print("best member: "+"".join([chr(e) for e in population[np.argmax(prob)]]))
    if all(population[np.argmax(prob)] == target):
        print("success")
        break
    child=crossover(dad)
    population=mutate(child)
