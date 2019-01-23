from pygame import draw

shape = __import__('program_variables').ProgramVariables.shape
tile_size = __import__('program_variables').ProgramVariables.tile_size
grey = __import__('program_variables').ProgramVariables.Colours.grey
white = __import__('program_variables').ProgramVariables.Colours.white


def draw_grid(display_surface):
    display_surface.fill((255, 255, 255))

    if shape[0] == shape[1]:
        for x in range(0, shape[0]):
            if x % tile_size == 0:
                draw.line(display_surface, grey, (x, 0), (x, shape[0] - 1), 1)
                draw.line(display_surface, grey, (0, x), (shape[0] - 1, x), 1)

    else:
        for x in range(0, shape[0]):
            if x % tile_size == 0:
                draw.line(display_surface, grey, (x, 0), (x, shape[1] - 1), 1)

        for y in range(0, shape[1]):
            if y % tile_size == 0:
                draw.line(display_surface, grey, (0, y), (shape[0] - 1, y), 1)



