
shape = __import__('program_variables').program_variables.shape


def draw_grid(display_surface):
    display_surface.fill((255, 255, 255))

    for x in range(0, shape[0]):
        for y in range(0, shape[1]):


