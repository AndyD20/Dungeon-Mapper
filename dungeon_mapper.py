import pygame
import sys

from draw_grid import draw_grid
from game_state import GameState
from program_variables import ProgramVariables
from pygame_helpers import initialise_pygame, running_loop
from timer import timer


def main():

    display_surface = timer('Initialisation', initialise_pygame)

    draw_grid(display_surface)

    ProgramVariables.game_state = GameState.RUNNING

    running_loop(display_surface)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
