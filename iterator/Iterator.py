from abc import ABC, abstractmethod


class Iterator(ABC):

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def current(self) -> object:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass
