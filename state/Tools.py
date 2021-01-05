from abc import ABC, abstractmethod


class Tool(ABC):
    """ Formal interface for implementing different tools to work with a canvas """

    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass


class SelectionTool(Tool):
    """ Tool for selection on a canvas. Implements the Tool interface """

    def __init__(self):
        pass

    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Draw a dashed rectangle")


class BrushTool(Tool):
    """ A brush Tool for drawing on a canvas. Implements the Tool interface """

    def __init__(self):
        pass

    def mouse_down(self):
        print("Brush icon")

    def mouse_up(self):
        print("Drawing on the canvas")
