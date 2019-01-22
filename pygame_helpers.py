import pygame
from pygame.locals import *
from program_variables import ProgramVariables
from game_state import GameState


def initialise_pygame():
    pygame.init()
    display_surface = pygame.display.set_mode((ProgramVariables.shape[0], ProgramVariables.shape[1]))
    pygame.display.set_caption(ProgramVariables.window_title)

    return display_surface


def running_loop():
    while ProgramVariables.game_state is GameState.RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                ProgramVariables.game_state = GameState.STOPPING
        pygame.display.update()
