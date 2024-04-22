# layout: a user provided string of comment separated Xs, Os, and #s in row major order
# self.layout: internal representation of board layout, 3x3 np array, 0 = # (empty), 1 = X, 2 = 0

import numpy as np
import re

class board:
    def __init__(self, layout: str):
        self.layout = np.zeros((3, 3))

        entries = re.split(r'\s?,\s?', layout)
        if len(entries) != 9:
            raise Exception("""
                            Invalid board provided. Specify a tic-tac-toe grid by giving a list of 9 vaulues in row major order.\n
                            Use #s to specify empty positions, Xs and Os or 0s.
                            """)
        
        for i in range(len(entries)):
            if entries[i] == "#":
                    self.layout[i//3, i%3] = 0
            elif entries[i] == "X":
                    self.layout[i//3, i%3] = 1
            elif entries[i] ==  "O" or entries[i] == "0":
                    self.layout[i//3, i%3] = 2

    def __str__(self):
        s = ""

        for i in range(3):
            for j in range(3):
                s += " "
                if self.layout[i, j] == 0:
                    s += " "
                elif self.layout[i, j] == 1:
                    s += "X"
                elif self.layout[i, j] == 2:
                    s += "O"
                s += " "
                s += "\n" if j == 2 else "|"
            if i != 2:
                s += "-----------\n"

        return s
    
    def XCount(self):
        return len(np.where(self.layout == 1)[0])
    
    def OCount(self):
        return len(np.where(self.layout == 2)[0])
    
    def blankCount(self):
        return 9 - (self.XCount() + self.OCount())
    
    def isValid(self):
        if len(self.layout) != 9:
            return False
        
        if self.XCount < 0 or self.OCount < 0:
            return False
        
        if self.XCount < self.OCount:
            return False
        
        if self.XCount > self.OCount + 1:
            return False
        
        if self.isXTurn() == self.isOTurn():
            return False

        return True
    
    def isXTurn(self):
        if self.XCount() == 0 and self.OCount() == self.OCount():
            return True
        return self.XCount() == self.OCount() and self.XCount() + 1 - self.OCount() < 2
    
    def isOTurn(self):
        if self.XCount() == 0 and self.XCount() == self.OCount():
            return False
        return self.XCount() == self.OCount() + 1 and self.OCount() + 1 == self.XCount()

    def placeX(self, pos):
        if not self.isXTurn():
            print("It is not Xs turn!")
            return False
        
        if pos[0] < 0 or pos[0] > 2:
            print("Out of bounds!")
            return False
        
        if pos[1] < 0 or pos[1] > 2:
            print("Out of bounds!")
            return False 
        
        if self.layout[pos[0], pos[1]] != 0:
            print("That space is not empty!")
            return False
        else:
            self.layout[pos[0], pos[1]] = 1
            print(self)
            return True

    def placeO(self, pos):
        if not self.isOTurn():
            print("It is not Os turn!")
            return False
        
        if pos[0] < 0 or pos[0] > 2:
            print("Out of bounds!")
            return False
        
        if pos[1] < 0 or pos[1] > 2:
            print("Out of bounds!")
            return False 
        
        if self.layout[pos[0], pos[1]] != 0:
            print("That space is not empty!")
            return False
        else:
            self.layout[pos[0], pos[1]] = 2
            print(self)
            return True

    def clearBoard(self):
        self.layout = np.zeros((3, 3))

board1 = board("#,#,#,#,#,#,#,#,#")
print(board1.XCount())
print(board1.OCount())

board1.placeO((0, 0))
board1.placeX((0, 0))
board1.placeO((1, 1))
board1.placeX((1, 1))
board1.placeO((1, 1))
board1.placeX((1, 2))
board1.placeX((2, 1))
board1.placeO((1, 3))
board1.placeX((1, 1))
board1.placeO((0, 2))
board1.placeX((2, 0))
board1.placeO((0, 1))
board1.placeX((2, 2))