


import GameState.GameState as gs

import pygame



class GameInfomation():
    def __init__(self):
        self.currentState = gs.GAME_INIT

        # pygame initialize
        pygame.init()
        pygame.display.set_caption("game")
        self.screen = pygame.display.set_mode((1024,768),pygame.FULLSCREEN,32)
        # self.screen = pygame.display.set_mode(pygame.FULLSCREEN,0,32)
        # self.screen = pygame.display.set_mode(pygame.FULLSCREEN)
        self.pygame = pygame



        self.fps = 30
