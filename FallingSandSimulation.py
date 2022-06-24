import numpy
import pygame.display
from pygame import *
import numpy as np

"""Simulation of falling sand"""


class FallingSand:
    """Class of falling sand"""

    def __init__(self):

        # screen and sizes
        self.row = 55
        self.col = 100
        self.size = 6
        self.screen = pygame.display.set_mode((self.col*self.size, self.row*self.size))
        pygame.display.set_caption("Falling Sand")

        # colors
        self.sandColor = (76, 69, 50)
        self.black = (0, 0, 0)

        self.run = True
        self.FPS = 120
        self.clock = pygame.time.Clock()

        self.array = np.zeros((self.row, self.col))

    def checkInIt(self, l, r,c):
        """Check in it"""
        try:
            l.index([r, c])
            return True
        except:
            return False

    def moveDown(self):
        """Move Down the sand pieces"""
        dontCheck = []

        for r in range(self.row):
            for c in range(self.col):
                if r != self.row-1 and c != self.col-1:
                    if self.array[r][c] == 1:
                        if self.checkInIt(dontCheck, r, c) is False:
                            # check empty

                            if self.array[r+1][c] == 0:  # check down
                                self.array[r+1][c] = 1
                                self.array[r][c] = 0
                                dontCheck.append([r+1, c])
                            elif self.array[r+1][c+1] == 0:  # down rigth
                                self.array[r+1][c+1] = 1
                                self.array[r][c] = 0
                                dontCheck.append([r+1, c-1])
                            elif self.array[r+1][c-1] == 0 and c-1 >= 0:  # down left
                                self.array[r+1][c-1] = 1
                                self.array[r][c] = 0
                                dontCheck.append([r+1, c+1])

    def event(self):
        """Event loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            key = pygame.key.get_pressed()
            if pygame.mouse.get_pressed(3)[0] or key[pygame.K_SPACE] == 1:
                x, y = pygame.mouse.get_pos()

                for r in range(self.row):
                    for c in range(self.col):
                        if (self.size*c <= x <= self.size*(c+1)) and (self.size*r <= y <= self.size*(r+1)):
                            self.array[r][c] = 1


    def main(self):
        """Main Function"""
        while self.run is True:
            self.event()
            self.moveDown()
            self.draw()

    def drawBlocks(self):
        """Draw Blocks"""

        for r in range(self.row):
            for c in range(self.col):
                if self.array[r][c] == 1:
                    pygame.draw.rect(self.screen, self.sandColor, pygame.Rect((c*self.size, r*self.size), (self.size, self.size)))
                else:
                    pygame.draw.rect(self.screen, self.black, pygame.Rect((c * self.size, r * self.size), (self.size, self.size)))


    def draw(self):
        """Draw screen"""
        self.screen.fill(self.black)
        self.drawBlocks()
        pygame.display.flip()


if __name__ == '__main__':
    FallingSand().main()

