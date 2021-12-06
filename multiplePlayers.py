from random import random

def simulatedChampionshipWinner(players):
    reset(players)
    championshipEnd = False
    master = 0
    numPlayers = len(players)
    challengers = players.copy()
    challengers.pop(0)
    # print(players[master].winsInARow)
    while not championshipEnd:
    
        participant = challengers.pop(0)
        # print(master, participant.index, challengers[0].index)
        if simulatedMatchWinner(participant, players[master]) == master:
            players[master].addWin()
            challengers.append(participant)
            # print(challengers[0].index, challengers[1].index)
            if isChampion(players[master], numPlayers):
                # print(master, "is champions with", players[master].winsInARow, len(players))
                return master        
        else:
            if simulatedMatchWinner(participant, players[master]) == participant.index:
                players[master].restartCounter()
                challengers.append(players[master])
                # print(challengers[0].index, challengers[1].index)
                master = participant.index

            else:
                players[master].addWin()
                challengers.append(participant)
                # print(challengers[0].index, challengers[1].index)
                if isChampion(players[master], numPlayers):
                    # print(master, "is champions with", players[master].winsInARow, len(players))
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