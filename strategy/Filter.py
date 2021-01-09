from abc import ABC, abstractmethod


class Filter(ABC):

    @abstractmethod
    def apply(self, fileName: str) -> None:
        pass


class BlackAndWhiteFilter(Filter):

    def apply(self, fileName: str) -> None:
        print("applying the black and white filter " + fileName)


class SepalFilter(Filter):

    def apply(self, fileName: str) -> None:
        print("applying the sepal filter to " + fileName)
