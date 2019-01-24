from pygame import draw
from math import floor

black = __import__('program_variables').ProgramVariables.Colours.black
red = __import__('program_variables').ProgramVariables.Colours.red

def_line_size = __import__('program_variables').ProgramVariables.tile_size

def_line_size = floor(def_line_size / 5)


class DrawableLine:
    def __init__(self, start_pos, end_pos, is_completed_line):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.is_completed_line = is_completed_line

    def draw_line(self, display_surface):
        draw.line(
            display_surface,
            black if self.is_completed_line else red,
            (self.start_pos[0], self.start_pos[1]),
            (self.end_pos[0], self.end_pos[1]),
            def_line_size
        )
