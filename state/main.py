from canvas import Canvas
from tools import SelectionTool


def main() -> None:

    canvas = Canvas()

    canvas.mouse_down()
    canvas.mouse_up()

    canvas.set_current_tool(SelectionTool())

    canvas.mouse_down()
    canvas.mouse_up()


if __name__ == '__main__':
    main()
