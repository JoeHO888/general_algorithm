import numpy as np

length=np.random.randint(1,10,size=1)[0] # 10 is max length
crossover_rate=0.8
mutation_rate=0.01
generation=200
population_size=500
compare_times=100

target=np.random.randint(33,127,size=length)



def fitness(member):
    return length-np.count_nonzero(member-target)

def crossover(pop):
    for k in range(compare_times):
        i=np.random.randint(0,population_size,size=1)[0]
        j=np.random.randint(0,population_size,size=1)[0]
        if  np.random.uniform(0,1,1)<crossover_rate:
            if fitness(pop[i])>fitness(pop[j]):
                winner=pop[i]
                loser=pop[j]
            else:
                winner=pop[j]
                loser=pop[i]
            crosspoint=np.random.randint(0,length,size=1)[0]
            loser[crosspoint:]=winner[crosspoint:]
            loser=mutate(loser)
    return pop

def mutate(member):
    for i in range(len(member)):
            if np.random.uniform(0,1,1)<mutation_rate:
                member[i]=np.random.randint(33,127,size=1)
    return member

    
print("target: "+"".join([chr(e) for e in target]))

population=np.random.randint(33,127,size=(population_size,length))

i=1                  
while True:
    fitness_list=[fitness(e) for e in population]
    print("generation: "+str(i))
    print("best member: "+"".join([chr(e) for e in population[np.argmax(fitness_list)]]))
    if all(population[np.argmax(fitness_list)] == target):
        print("success")
        break
    child=crossover(population)
    i=i+1
