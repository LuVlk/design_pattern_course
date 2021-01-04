import Tools as tls


class Canvas:
    # think of a Canvas in a drawing application

    def __init__(self) -> None:
        self.__currentTool: tls.Tool = tls.BrushTool()

    def mouseDown(self) -> None:
        self.__currentTool.mouseDown()

    def mouseUp(self) -> None:
        self.__currentTool.mouseUp()

    def setCurrentTool(self, tool: tls.Tool) -> None:
        self.__currentTool = tool