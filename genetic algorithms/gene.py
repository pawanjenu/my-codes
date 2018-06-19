from fuzzywuzzy import fuzz
import random
import string
let = 'qwertyuiopasdfghjklzxcvbnm'

class pop:
    
    
    def __init__(self,len):
        self.string = ''.join(random.choice(let) for _ in range(len))
        self.fit = -1

    def __str__(self):
        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fit)

target = None
target_len = None
population = 20
gen = 1000

def ini_pop(population,len):
    
    #agent = []
    return[ pop(len) for _ in range(population)]
        

def fitness(agents):
    score = 0
    '''for agent in agents:
        agent.fit = fuzz.ratio(agent.string,target_len)'''
    for agent in agents:
        score = 0
        for x in range(len(target)):
           if agent.string[x] == target[x]:
                score+=1
        agent.fit = (score/target_len)*100
    return agents
        
    
                
    #agent.fit = score

    return agents

def selection(agents):
    
    agents = sorted(agents, key=lambda agent: agent.fit, reverse=True)
    print('\n'.join(map(str, agents)) )
    agents = agents[:int(0.2 * len(agents))]

    return agents

def cross(agents):
    newstr = []
    for _ in range((population - len(agents))//2):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = pop(target_len)
        split = target_len//2
        child1.string = parent1.string[0:split] + parent2.string[split:target_len]

        newstr.append(child1)

    agents.extend(newstr)

    return agents

def mutation(agents):
    for x in agents:
        for a,b in enumerate(x.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                x.string = x.string[0:a] + random.choice(let) + x.string[a+1:target_len]


    return agents




    

def galgo():
    agents = ini_pop(population,target_len)

    for x in range(gen):
        print("generation:",x)
        agents = fitness(agents)
        agents = selection(agents)
        agents = cross(agents)
        agents = mutation(agents)
        for agent in agents:
            if agent.string == target:
                print("best result:",agent.string)
                exit(0)

        #if any(agent.fit >= 90 for agent in agents):
            
    
         #   print('Threshold met!')
         #   exit(0)


if __name__ == '__main__':
    
    target = str(input("enter the string:"))
    
    #target = 'pawan'
    target_len = len(target)
    galgo()

    
