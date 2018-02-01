import numpy as np

class population:
    def __init__(self, length, crossover_rate, mutation_rate, generation, population_size, population,compare_time):
        self.length=length
        self.crossover_rate=crossover_rate
        self.mutation_rate=mutation_rate
        self.generation=generation
        self.population_size=population_size
        self.population=population
        self.compare_time=compare_time
    def fitness(self, member):
        return self.length-np.count_nonzero(member-target)

    def crossover(self,pop):
        for k in range(self.compare_time):
            if  np.random.uniform(0,1,1)<self.crossover_rate:
                i=np.random.randint(0,self.population_size,size=1)[0]
                j=np.random.randint(0,self.population_size,size=1)[0]
                if self.fitness(pop[i])>self.fitness(pop[j]):
                    winner=pop[i]
                    loser=pop[j]
                else:
                    winner=pop[j]
                    loser=pop[i]
                crosspoint=np.random.randint(0,self.length,size=1)[0]
                loser[crosspoint:]=winner[crosspoint:]
                loser=self.mutate(loser)
        return pop

    def mutate(self,member):
        for i in range(len(member)):
                if np.random.uniform(0,1,1)<self.mutation_rate:
                    member[i]=np.random.randint(33,127,size=1)
        return member
    
length_=np.random.randint(1,10,size=1)[0] # 10 is max length
crossover_rate_=0.8
mutation_rate_=0.01
generation_=200
population_size_=500
compare_time_=100

target=np.random.randint(33,127,size=length_)   
print("target: "+"".join([chr(e) for e in target]))

population_=np.random.randint(33,127,size=(population_size_,length_))

experiment_population=population(length_,crossover_rate_,mutation_rate_, generation_,population_size_,population_, compare_time_)
i=1                  
while True:
    fitness_list=[experiment_population.fitness(e) for e in experiment_population.population]
    print("generation: "+str(i))
    print("best member: "+"".join([chr(e) for e in experiment_population.population[np.argmax(fitness_list)]]))
    if all(experiment_population.population[np.argmax(fitness_list)] == target):
        print("success")
        break
    child=experiment_population.crossover(experiment_population.population)
    experiment_population=population(length_,crossover_rate_,mutation_rate_, generation_,population_size_,child, compare_time_)
    i=i+1
