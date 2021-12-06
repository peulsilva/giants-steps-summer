class Player:
    def __init__(self, skill, index) -> None:
        self.skill= skill
        self.index = index
        self.winsInARow= 0

    def addWin(self):
        self.winsInARow += 1
    
    def restartCounter(self):
        self.winsInARow= 0
