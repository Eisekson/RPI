import GameInfomation as gi

from GameState import GameState as gs
import GameState.Game.Game as game


# from GameState.Game import GameInit
import GameState.Game.Game

gameInfo = gi.GameInfomation()

pygame = gameInfo.pygame
clock = pygame.time.Clock()


def GameLoop():
    done = True
    while done:
        clock.tick(gameInfo.fps)
        pygame = gameInfo.pygame
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key == 'q'):
                    done = False
            # if event.type == pygame.QUIT:
            #     If user clicked close
                # done = False  # Flag that we are done so we exit this loop

        if gameInfo.currentState is gs.GAME_INIT:
            game.init(gameInfo)
            print 'game init'
        if gameInfo.currentState is gs.GAME_PLAY:
            game.play(gameInfo)
            print 'game play'


