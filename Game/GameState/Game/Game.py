

import GameInfomation as gi
import pygame

def init(gameInfo):

    gameInfo.screen.fill((255,255,255))
    gameInfo.pygame.display.flip()
    gameInfo.currentState = gi.gs.GAME_PLAY
    print 'game init model'

def play(gameInfo):

    # gameInfo.currentState = gi.gs.GAME_CHANGE
    gameInfo.screen.fill((0,0,0))
    pygame.display.flip()
    print 'game play model'

def exit():
    print 'game exit model'
