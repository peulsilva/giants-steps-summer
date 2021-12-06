def twoPlayers(x, y):
    j1 = x/(x+y)
    j2 = 1- j1

    pRei = j1**2 

    return (j1 + j1 * j2)/(1-j2**2*pRei)

