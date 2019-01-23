from pygame import draw
from pygame.locals import *
from program_variables import ProgramVariables
from game_state import GameState
from draw_grid import draw_grid
from drawable_line import DrawableLine

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

        for line in drawn_lines:
            if not line.is_completed_line:
                drawn_lines.remove(line)

        if draw_line:
            drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), False))

        if event.type == MOUSEBUTTONUP and draw_line:

            drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), True))
            draw_line = False
            line_begin = (0, 0)

        draw_grid(display_surface)

        for line in drawn_lines:

            line_color = black

            if not line.is_completed_line:
                line_color = red

            draw.line(
                display_surface,
                line_color,
                (line.start_pos[0], line.start_pos[1]),
                (line.end_pos[0], line.end_pos[1]),
                1
            )
