# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015

@author: Bryce Albertazzi
"""

import Dominion
import random
from collections import defaultdict
import testUtility



#Define box
box = testUtility.GetBoxes()

supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)

############Test 1 Bug###################
random10 = boxlist[:15] #Should be random10 = boxlist[:10]
#########################################

supply = defaultdict(list,[(k,box[k]) for k in random10])


#Give the supply its designated cards
testUtility.SetSupply(supply)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.ConstructPlayerObjects()

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)