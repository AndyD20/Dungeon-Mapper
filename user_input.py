from pygame import draw
from pygame.locals import *
from program_variables import ProgramVariables
from game_state import GameState
from draw_grid import draw_grid

black = __import__('program_variables').ProgramVariables.Colours.black
red = __import__('program_variables').ProgramVariables.Colours.red
mouse_position = __import__('pygame').mouse.get_pos


draw_line = False
line_begin = (0, 0)
drawn_lines = []


def check_for_user_input(events, display_surface):

    m_pos = mouse_position()

    global draw_line
    global line_begin

    for event in events:
        if event.type == QUIT:
            ProgramVariables.game_state = GameState.STOPPING

        if event.type == MOUSEBUTTONDOWN:
            draw_line = True
            line_begin = event.pos

        if draw_line:
            draw_grid(display_surface)
            draw.line(display_surface, red, (line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), 1)

        if event.type == MOUSEBUTTONUP and draw_line:

            draw_grid(display_surface)
            draw_line = False
            draw.line(
                display_surface,
                black,
                (line_begin[0], line_begin[1]),
                (event.pos[0], event.pos[1]),
                1
            )
            line_begin = (0, 0)
