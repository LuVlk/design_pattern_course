from Canvas import Canvas
from Tools import SelectionTool


def main() -> None:

    C = Canvas()

    C.mouseDown()
    C.mouseUp()

    C.setCurrentTool(SelectionTool())

    C.mouseDown()
    C.mouseUp()


if __name__ == '__main__':
    main()