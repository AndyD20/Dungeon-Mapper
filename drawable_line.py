from pygame import draw
from math import floor
from drawable_object import DrawableObject
from drawable_details import DrawableDetails

black = __import__('program_variables').ProgramVariables.Colours.black
red = __import__('program_variables').ProgramVariables.Colours.red

def_line_size = __import__('program_variables').ProgramVariables.tile_size
def_line_size = floor(def_line_size / 5)


class DrawableLine(DrawableObject):
    def __init__(self, start_pos, end_pos, is_completed_line):
        self.details = DrawableDetails(start_pos, end_pos, is_completed_line)

    def draw_self(self, display_surface):
        draw.line(
            display_surface,
            black if self.details.is_completed else red,
            (self.details.start_pos[0], self.details.start_pos[1]),
            (self.details.end_pos[0], self.details.end_pos[1]),
            def_line_size
        )
