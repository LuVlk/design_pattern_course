class Document:

    def __init__(self):
        self.__content = ""
        self.__font = Font()

    def __str__(self):
        return (
            "content: " + self.__content +
            " " + str(self.__font)
        )

    def __repr__(self):
        return "Document(\"" + self.__content + "\", " + repr(self.__font) + ")"

    def setContent(self, content: str):
        self.__content = content

    def getContent(self):
        return self.__content

    def setFont(self, name: str, size: int):
        self.__font = Font(name, size)

    def getFont(self):
        return self.__font


class Font:

    def __init__(self, name: str = "", size: int = 0) -> None:
        self.__fontName = name
        self.__fontSize = size

    def __str__(self):
        return (
            "fontName: " + self.__fontName + 
            " fontSize: " + str(self.__fontSize)
        )

    def __repr__(self):
        return "Font(\"" + self.__fontName + "\", " + str(self.__fontSize) + ")"

    