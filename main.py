
# IA Q-learning

import numpy as np
import random
import time
import matplotlib.pyplot as plt

# init IA Q-learning:

# Initialisation de la table Q

NOMBRE_ALUMETTES = 25
NOMBRE_ENTRAINEMENT = 20000

Q = np.zeros((NOMBRE_ALUMETTES+1, 4)) 



class Robot():

    def __init__(self, name, epsilon=0.1):
        self.name = name
        self.epsilon = epsilon

    def play(self, nb_allu_total, learn=True):
        nb_allu_total = int(nb_allu_total)
        if random.uniform(0, 1) < self.epsilon and learn:
            nb_allu_recup = random.randint(1, min(3, nb_allu_total))
        else: 
            nb_allu_recup = np.argmax(Q[nb_allu_total, 1:]) + 1 


        nb_allu_recup = int(nb_allu_recup)
        if not learn:
            print(f"{self.name} retire {nb_allu_recup} allumettes")

        else:
            addHistorique(self.name, nb_allu_total, nb_allu_recup)

        return nb_allu_recup
    


def update_Q_table(historiqueGame, robotWin):
    alpha = 0.1
    gamma = 0.8
    reward_win = 1
    reward_lose = -1

    for robot, etats_actions in historiqueGame.items():
        for i in range(len(etats_actions) - 1):
            s, a = etats_actions[i]
            s = int(s) 
            a = int(a) 
            s_next, _ = etats_actions[i + 1]
            s_next = int(s_next) 
                
            reward = reward_win if robot == robotWin else reward_lose


            Q[s, a] = Q[s, a] + alpha * (reward + gamma * np.max(Q[int(s_next), 1:]) - Q[s, a])

        s_final, a_final = etats_actions[-1]
        s_final = int(s_final)
        a_final = int(a_final)
        Q[s_final, a_final] = Q[s_final, a_final] + alpha * (reward - Q[s_final, a_final])



def addHistorique(robot, nb_allu, nb_allu_recup):
    nb_allu = int(nb_allu)
    if historiqueGame.get(robot) is None:
        historiqueGame[robot] = [(nb_allu, nb_allu_recup)]
    else:
        historiqueGame[robot].append((nb_allu, nb_allu_recup))


def addStat(robotWin, historiqueGame):

    for elemRobot in historiqueGame:
        
        for elem in historiqueGame[elemRobot]:

            if elem == 1 and robotWin == elemRobot:
                pass

            if stat.get(elem) == None:
                stat[elem] = [ 1 if robotWin == elemRobot else 0]
            else:
                stat[elem].append(1 if robotWin == elemRobot else 0)

    return stat


stat = {}  

robot1 = Robot("robot1")
robot2 = Robot("robot2")


for nombreGame in range(NOMBRE_ENTRAINEMENT):

    robotWin = robot1.name

    nb_allu = NOMBRE_ALUMETTES
    historiqueGame = {}


    while nb_allu > 0:

        nb_allu = nb_allu - robot1.play(nb_allu)

        if nb_allu > 0:
            nb_allu = nb_allu - robot2.play(nb_allu)
        else:
            robotWin = robot2.name
            break

    update_Q_table(historiqueGame, robotWin)
    robot1.epsilon = max(0.01, robot1.epsilon * 0.999)
    robot2.epsilon = max(0.01, robot2.epsilon * 0.999)


    stat = addStat(robotWin, historiqueGame)

    if nombreGame % (NOMBRE_ENTRAINEMENT/10) == 0:
        print(f"Nombre de parties : {nombreGame*100/NOMBRE_ENTRAINEMENT} %") 

# print(stat)
print(stat.get(1))

moyenneVictoire = {}

# calcul de la moyenne de victoire pour chaque nombre d'allumettes restantes
for elem in stat:
    
    moyenneVictoire[elem] = sum(stat[elem]) / len(stat[elem])

print("\nSTAT\n")
for elem in dict(reversed(sorted(moyenneVictoire.items()))):
    print(f"{elem} : {moyenneVictoire[elem]}")

print("\n\n\n\n\n\n")
    
# go play with the robot
win = "joueur"
nb_allu = NOMBRE_ALUMETTES
while nb_allu > 0:
    
    print("Il reste " + str(nb_allu) + " allumettes")
    nb_allu -= int(input("Combien d'allumettes voulez-vous retirer ? "))

    if nb_allu > 0:
        nb_allu = nb_allu - robot1.play(nb_allu, False)
    else:
        win = "robot1"
        break

print(f"Le gagnant est {win}")

