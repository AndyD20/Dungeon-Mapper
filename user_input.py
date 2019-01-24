from pygame.locals import *

from draw_grid import draw_grid
from drawable_line import DrawableLine
from game_state import GameState
from program_variables import ProgramVariables

mouse_position = __import__('pygame').mouse.get_pos

grid_lock = False
draw_line = False
line_begin = (0, 0)
drawn_lines = []


def check_for_user_input(events, display_surface):
    global draw_line
    global line_begin
    global grid_lock

    for event in events:
        if event.type == QUIT:
            ProgramVariables.game_state = GameState.STOPPING

        if event.type == KEYUP:
            if event.key == K_l:
                grid_lock = not grid_lock
                print(grid_lock)

        if event.type == MOUSEBUTTONDOWN:
            mouse_down(event)

        old_line_cleanup()

        if event.type == MOUSEBUTTONUP and draw_line:
            mouse_up()

        redraw_grid(display_surface)


def redraw_grid(display_surface):
    draw_grid(display_surface)
    for line in drawn_lines:
        line.draw_line(display_surface)


def mouse_down(event):
    global draw_line
    global line_begin

    draw_line = True
    line_begin = event.pos


def old_line_cleanup():
    m_pos = mouse_position()

    for line in drawn_lines:
        if not line.is_completed_line:
            drawn_lines.remove(line)

    if draw_line:
        drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), False))


def mouse_up():
    global draw_line
    global line_begin

    m_pos = mouse_position()

    drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), True))
    draw_line = False
    line_begin = (0, 0)
