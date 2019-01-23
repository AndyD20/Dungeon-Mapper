from pygame import draw
from pygame.locals import *

black = __import__('program_variables').ProgramVariables.Colours.black


class UserInputVariables:
    begin_draw_line = False
    start_line_pos = (0, 0)


def check_for_user_input(event, display_surface):
    if event.type == MOUSEBUTTONDOWN:
        UserInputVariables.begin_draw_line = True
        UserInputVariables.start_line_pos = event.pos

    if event.type == MOUSEBUTTONUP and UserInputVariables.begin_draw_line:
        UserInputVariables.begin_draw_line = False
        draw.line(
            display_surface,
            black,
            (UserInputVariables.start_line_pos[0], UserInputVariables.start_line_pos[1]),
            (event.pos[0], event.pos[1]),
            1
        )
        UserInputVariables.start_line_pos = (0, 0)
