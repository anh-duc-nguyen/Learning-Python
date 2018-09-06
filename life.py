'''
Remake Conway's Game of Life
'''
# import numpy as np
class Gaia:
    def __init__(self):
        H = 5
        W = 5
        self.board =[]
        for i in range(H):
            line = []
            for j in range(W):
                p = Particle(i,j)
                line.append(p)
            self.board.append(line)
    def show(self):
        for i in self.board:
            line =''
            for j in i:
                line += j.toString()
            print(line)

class Particle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = 0
    def toString(self):
        return str(self.state)

def main():
    earth = Gaia()
    earth.show()

if __name__ == '__main__':
    main()