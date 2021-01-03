from EditorState import EditorState


class Editor:

    def __init__(self):
        self.__content = ""

    def __str__(self):
        return "content: " + self.__content

    def createState(self):
        return EditorState(self.__content)

    def restore(self, state):
        self.__content = state.getContent()

    def getContent(self):
        return self.__content

    def setContent(self, content):
        self.__content = content
