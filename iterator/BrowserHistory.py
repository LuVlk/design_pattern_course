from History import History
from Iterator import Iterator
from typing import List


class BrowserHistory(History):

    def push(self, url: str) -> None:
        super().push(url)

    def create_iterator(self):
        return self.HistoryIterator(super(), str())

    def _get_states(self):
        return super().get_states(str)

    class HistoryIterator(Iterator):

        def __init__(self, history: History, obj: object) -> None:
            self.__elements: List[object] = history.get_states(obj)
            self.__index: int = len(self.__elements) - 1
            self.__current: object = self.__elements[self.__index]

        def next(self) -> None:
            self.__current = self.__elements[self.__index - 1]
            self.__index -= 1

        def current(self) -> object:
            return self.__current

        def has_next(self):
            return not (self.__index < 0)
