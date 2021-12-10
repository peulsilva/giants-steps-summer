from random import random

def simulatedChampionshipWinner(players):
    reset(players)
    championshipEnd = False
    master = 0
    numPlayers = len(players)
    challengers = players.copy()
    challengers.pop(0)
    while not championshipEnd:
    
        participant = challengers.pop(0)
        if simulatedMatchWinner(participant, players[master]) == master:
            players[master].addWin()
            challengers.append(participant)
            if isChampion(players[master], numPlayers):
                return master        
        else:
            if simulatedMatchWinner(participant, players[master]) == participant.index:
                players[master].restartCounter()
                challengers.append(players[master])
                master = participant.index

            else:
                players[master].addWin()
                challengers.append(participant)
                if isChampion(players[master], numPlayers):
                    return master
    

def simulatedMatchWinner(player, master):
    if random() < player.skill/(player.skill+ master.skill):
        return player.index
    return master.index

def isChampion(master, numPlayers):
    if master.winsInARow >= numPlayers -1:
        return True
    return False

def reset(players):
    for i in range(len(players)):
        players[i].restartCounter()