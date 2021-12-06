import time
from monteCarlo import monteCarlo
from player import Player
from plotDistribution import plotDistribution
from twoPlayers import twoPlayers

def main():
    t0= time.time()
    file = open("campeonatos.txt","r")
    writeFile = open("resultados.txt","w")
    for line in file:
        line = line.split("\n")[0]
        players = list(map(int, line.split(" ")))
        
        if len(players) == 2:
            probability = twoPlayers(players[0], players[1])
            print(players, probability)
        else:
            playersArray = []
            for i in range(len(players)):
                playersArray.append(Player(skill= players[i], index=i))
            probability, distribution = monteCarlo(playersArray)
            print(players, probability)
           
            if distribution:
                plotDistribution(distribution, str(players))
        writeFile.write(f"{str(probability)} \n")
    t1= time.time()

    print(f"execution time: {(t1-t0)/60} minutes")


if __name__ == "__main__": 
    main()    