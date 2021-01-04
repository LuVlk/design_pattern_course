from abc import ABC, abstractmethod


class Tool(ABC):
    """ Formal interface for implementing different tools to work with a canvas """

    @abstractmethod
    def mouseDown(self):
        pass

    @abstractmethod
    def mouseUp(self):
        pass


class SelectionTool(Tool):
    """ Tool for selection on a canvas. Implements the Tool interface """

    def __init__(self):
        pass

    def mouseDown(self):
        print("Selection icon")

    def mouseUp(self):
        print("Draw a dashed rectangle")


class BrushTool(Tool):
    """ A brush Tool for drawing on a canvas. Implements the Tool interface """

    def __init__(self):
        pass

    def mouseDown(self):
        print("Brush icon")

    def mouseUp(self):
        print("Drawing on the canvas")