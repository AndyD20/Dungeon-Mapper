from pygame.locals import *

from draw_grid import draw_grid
from drawable_line import DrawableLine
from game_state import GameState
from program_variables import ProgramVariables

mouse_position = __import__('pygame').mouse.get_pos
tile_size = __import__('program_variables').ProgramVariables.tile_size

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
            handle_keys(event)

        if event.type == MOUSEBUTTONDOWN:
            mouse_down(event)

        old_line_cleanup()

        if event.type == MOUSEBUTTONUP and draw_line:
            mouse_up()

        redraw_grid(display_surface)


def handle_keys(event):
    global grid_lock

    if event.key == K_l:
        grid_lock = not grid_lock


def redraw_grid(display_surface):
    draw_grid(display_surface)
    for line in drawn_lines:
        line.draw_line(display_surface)


def mouse_down(event):
    global draw_line
    global line_begin
    global grid_lock

    draw_line = True

    if not grid_lock or (event.pos[0] % tile_size == 0 and event.pos[1] % tile_size == 0):
        line_begin = event.pos
    else:
        x = round_number_to_nearest_grid_location(event.pos[0])
        y = round_number_to_nearest_grid_location(event.pos[1])
        line_begin = (x, y)


def old_line_cleanup():
    m_pos = mouse_position()

    for line in drawn_lines:
        if not line.is_completed_line:
            drawn_lines.remove(line)

    if draw_line and not grid_lock:
        drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), False))
    elif draw_line:
        x = round_number_to_nearest_grid_location(line_begin[0])
        y = round_number_to_nearest_grid_location(line_begin[1])
        x2 = round_number_to_nearest_grid_location(m_pos[0])
        y2 = round_number_to_nearest_grid_location(m_pos[1])
        drawn_lines.append(DrawableLine((x, y), (x2, y2), False))


def mouse_up():
    global draw_line
    global line_begin

    m_pos = mouse_position()
    if not grid_lock:
        drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), True))
    else:
        x = round_number_to_nearest_grid_location(m_pos[0])
        y = round_number_to_nearest_grid_location(m_pos[1])
        drawn_lines.append(DrawableLine((line_begin[0], line_begin[1]), (x, y), True))

    draw_line = False
    line_begin = (0, 0)


def round_number_to_nearest_grid_location(num):
    return int(tile_size * round(float(num)/tile_size))
