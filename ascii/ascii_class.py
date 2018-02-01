import numpy as np

class population:
    def __init__(self, length, crossover_rate, mutation_rate, generation, population_size, population):
        self.length=length
        self.crossover_rate=crossover_rate
        self.mutation_rate=mutation_rate
        self.generation=generation
        self.population_size=population_size
        self.population=population
    def fitness(self, member):
        return self.length-np.count_nonzero(member-target)

    def select(self,pop):
        probability=np.array([pop.fitness(e) for e in pop.population])
        index=np.random.choice(self.population_size, self.population_size, replace=True,p=probability/probability.sum())
        return [probability,np.array([pop.population[i] for i in index])]

    def crossover(self, parent):
        for e in parent:
            if  np.random.uniform(0,1,1)<self.crossover_rate:
                crosspoint=np.random.randint(0,self.length,size=1)[0]
                i=np.random.randint(0,self.population_size,size=1)[0]
                e[crosspoint:]=self.population[i,crosspoint:][np.newaxis,:]
        return parent

    def mutate(self,pop):
        for e in pop:
            for i in range(len(e)):
                if np.random.uniform(0,1,1)<self.mutation_rate:
                    e[i]=np.random.randint(33,127,size=1)
        return pop

length_=np.random.randint(1,50,size=1)[0] # 10 is max length
crossover_rate_=0.8
mutation_rate_=0.01
generation_=200
population_size_=500

target=np.random.randint(33,127,size=length_)   
print("target: "+"".join([chr(e) for e in target]))

population_=np.random.randint(33,127,size=(population_size_,length_))

experiment_population=population(length_,crossover_rate_,mutation_rate_, generation_,population_size_,population_)

i=0
while True:
    i+=1
    prob, dad=experiment.select(experiment_population)
    print("generation: "+str(i))
    print("best member: "+"".join([chr(e) for e in experiment_population.population[np.argmax(prob)]]))
    if all(experiment_population.population[np.argmax(prob)] == target):
        print("success")
        break
    child=experiment_population.crossover(dad)
    child=experiment_population.mutate(child)
    experiment_population=population(length_,crossover_rate_,mutation_rate_, generation_,population_size_,child)
