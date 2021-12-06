import matplotlib.pyplot as plt
import os

def plotDistribution(data, name):
    path = os.path.dirname(__file__)
    filename= os.path.join(path, "figures", name)
    plt.plot(data)
    plt.ylim(0,1)
    plt.title(f"Probabilidade acumulada do 1º mestre do mario kart ser campeão")
    plt.xlabel("Campeonatos simulados")
    plt.ylabel("Probabilidade acumulada")
    plt.savefig(filename)
    plt.close()
