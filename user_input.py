from pygame.locals import *

from draw_grid import draw_grid
from drawable_line import DrawableLine
from drawable_rectangle import DrawableRectangle
from game_state import GameState
from program_variables import ProgramVariables
from mouse_modes import MouseModes

mouse_position = __import__('pygame').mouse.get_pos
tile_size = __import__('program_variables').ProgramVariables.tile_size

grid_lock = False
draw_line = False
ctrl_down = False
undo_buffer = False
mouse_mode = MouseModes.STRAIGHT_LINE
line_begin = (0, 0)
drawn_objects = []


def check_for_user_input(events, display_surface):
    global draw_line
    global line_begin
    global grid_lock

    for event in events:
        if event.type == QUIT:
            ProgramVariables.game_state = GameState.STOPPING

        if event.type == KEYUP or event.type == KEYDOWN:
            handle_keys(event)

        if event.type == MOUSEBUTTONDOWN:
            mouse_down(event)

        old_line_cleanup()

        if event.type == MOUSEBUTTONUP and draw_line:
            mouse_up()

        redraw_grid(display_surface)


def handle_keys(event):
    global grid_lock
    global ctrl_down
    global undo_buffer
    global mouse_mode

    if event.key == K_l and event.type == KEYUP:
        grid_lock = not grid_lock
    elif event.key == K_LCTRL and event.type == KEYDOWN:
        ctrl_down = True
    elif event.key == K_LCTRL and event.type == KEYUP:
        ctrl_down = False
    elif event.key == K_z and event.type == KEYDOWN and ctrl_down:
        if not undo_buffer:
            if len(drawn_objects) is not 0:
                drawn_objects.pop()
                undo_buffer = True
    elif event.key == K_z and event.type == KEYUP and ctrl_down:
        undo_buffer = False
    elif event.key == K_d and event.type == KEYUP:
        mouse_mode = MouseModes.DOOR
    elif event.key == K_s and event.type == KEYUP:
        mouse_mode = MouseModes.STRAIGHT_LINE


def redraw_grid(display_surface):
    draw_grid(display_surface)
    for drawable_object in drawn_objects:
        drawable_object.draw_self(display_surface)


def mouse_down(event):
    global draw_line
    global line_begin
    global grid_lock

    draw_line = True

    if not grid_lock or (event.pos[0] % tile_size == 0 and event.pos[1] % tile_size == 0):
        line_begin = event.pos
    else:
        line_begin = round_coordinate_to_grid((event.pos[0], event.pos[1]))


def old_line_cleanup():
    for line in drawn_objects:
        if not line.details.is_completed:
            drawn_objects.remove(line)
    if draw_line:
        draw_an_object(is_completed_line=False)


def mouse_up():
    global draw_line
    global line_begin

    draw_an_object(is_completed_line=True)

    draw_line = False
    line_begin = (0, 0)


def draw_an_object(is_completed_line):
    m_pos = mouse_position()
    if grid_lock:
        draw_a_grid_locked_object(is_completed_line)
    else:
        if mouse_mode == MouseModes.STRAIGHT_LINE:
            drawn_objects.append(DrawableLine((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), is_completed_line))
        elif mouse_mode == MouseModes.DOOR:
            drawn_objects.append(
                DrawableRectangle((line_begin[0], line_begin[1]), (m_pos[0], m_pos[1]), is_completed_line))


def draw_a_grid_locked_object(is_completed_line):
    if mouse_mode == MouseModes.STRAIGHT_LINE:
        m_pos = mouse_position()
        x1, y1 = round_coordinate_to_grid((line_begin[0], line_begin[1]))
        x2, y2 = round_coordinate_to_grid((m_pos[0], m_pos[1]))
        drawn_objects.append(DrawableLine((x1, y1), (x2, y2), is_completed_line))
    elif mouse_mode == MouseModes.DOOR:
        m_pos = mouse_position()
        x1, y1 = round_coordinate_to_grid((line_begin[0], line_begin[1]))
        x2, y2 = round_coordinate_to_grid((m_pos[0], m_pos[1]))
        drawn_objects.append(
            DrawableRectangle((x1, y1), (x2, y2), is_completed_line))


def round_coordinate_to_grid(coordinate):
    x = round_number_to_nearest_grid_location(coordinate[0])
    y = round_number_to_nearest_grid_location(coordinate[1])
    return x, y


def round_number_to_nearest_grid_location(num):
    return int(tile_size * round(float(num) / tile_size))
