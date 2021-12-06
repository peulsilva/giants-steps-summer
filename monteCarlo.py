from multiplePlayers import simulatedChampionshipWinner

def monteCarlo(players):
    initialMaster=0
    numChampionships=0
    if len(players)<= 7:
        numChampionships = 100000
    else:
        return 0, []
    firstMasterWins = 0
    distribution = []
    for i in range(numChampionships):
        if simulatedChampionshipWinner(players) == initialMaster:
            firstMasterWins += 1
        distribution.append(firstMasterWins/(i+1))

    return firstMasterWins/numChampionships, distribution