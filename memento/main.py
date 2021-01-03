from Editor import Editor
from Document import Document
from History import History
from copy import deepcopy


history = History()


def editorTest():

    editor = Editor()

    print("adding new states \n")

    editor.setContent("a")
    history.push(editor.createState())
    print(str(editor))

    editor.setContent("b")
    history.push(editor.createState())
    print(str(editor))

    editor.setContent("c")
    history.push(editor.createState())
    print(str(editor))

    editor.setContent("d")
    print(str(editor))

    print("\nrestoring states \n")

    editor.restore(history.pop())
    print(str(editor))

    editor.restore(history.pop())
    print(str(editor))

    editor.restore(history.pop())
    print(str(editor))
    return


def documentTest():

    document = Document()

    print("adding new states \n")

    document.setContent("this is my first content")
    document.setFont("Times-New-Roman", 12)
    history.push(deepcopy(document))
    print(str(document))

    document.setContent("this is my second content")
    document.setFont("Arial", 14)
    history.push(deepcopy(document))
    print(str(document))

    document.setContent("this is my third content")
    document.setFont("Arial", 14)
    print(str(document))

    print("\nrestoring from history \n")

    # restoring from history
    document = history.pop()
    print(str(document))
    document = history.pop()
    print(str(document))
    document = history.pop()
    print(str(document))
    return


def combinedTest():

    document = Document()
    editor = Editor()

    print("adding new editor states")

    editor.setContent("a")
    history.push(editor.createState())
    print(str(editor))

    editor.setContent("b")
    print(str(editor))

    print("adding new document states")

    document.setContent("Hello World!")
    document.setFont("Times-New-Roman", 12)
    history.push(deepcopy(document))
    print(str(document))

    document.setContent("foo bar baz")
    document.setFont("Arial", 14)
    print(str(document))

    print("restoring from history")

    editor.restore(history.pop(editor.createState()))
    print(str(editor))

    document = history.pop(document)
    print(str(document))


def main():

    editorTest()

    print("---------------------------------")

    documentTest()

    print("---------------------------------")

    combinedTest()
    return


if __name__ == '__main__':
    main()