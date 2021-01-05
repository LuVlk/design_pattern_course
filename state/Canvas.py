import tools as tls


class Canvas:
    """ A canvas as for example found in a drawing application """

    def __init__(self) -> None:
        self.__current_tool: tls.Tool = tls.BrushTool()

    def mouse_down(self) -> None:
        self.__current_tool.mouse_down()

    def mouse_up(self) -> None:
        self.__current_tool.mouse_up()

    def set_current_tool(self, tool: tls.Tool) -> None:
        self.__current_tool = tool
