from pygame import draw
from math import floor
from drawable_object import DrawableObject
from drawable_details import DrawableDetails

dark_grey = __import__('program_variables').ProgramVariables.Colours.dark_grey
red = __import__('program_variables').ProgramVariables.Colours.red

tile_size = __import__('program_variables').ProgramVariables.tile_size
def_line_size = floor(tile_size / 5)


class DrawableRectangle(DrawableObject):
    def __init__(self, start_pos, end_pos, is_completed_line):
        self.details = DrawableDetails(start_pos, end_pos, is_completed_line)

    def draw_self(self, display_surface):
        width = self.details.end_pos[0] - self.details.start_pos[0]
        height = self.details.end_pos[1] - self.details.start_pos[1]

        #  Todo: find reliable way to position rectangles in the midpoints of grid locations when locked to grid
        rect_top = (self.details.start_pos[1] - (tile_size / 2)) + (floor(def_line_size / 2))
        rect = (self.details.start_pos[0] + 1, rect_top, width, height)

        draw.rect(
            display_surface,
            dark_grey if self.details.is_completed else red,
            rect,
            def_line_size
        )
