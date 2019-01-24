import abc


class DrawableObject(abc.ABC):
    @abc.abstractmethod
    def draw_self(self, display_surface):
        pass
