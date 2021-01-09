from abc import ABC, abstractmethod


class Compressor(ABC):

    @abstractmethod
    def compress(self, fileName: str) -> None:
        pass


class JPEGCompressor(Compressor):

    def compress(self, fileName: str) -> None:
        print("compressing " + fileName + " using JPEG")


class PNGCompressor(Compressor):

    def compress(self, fileName: str) -> None:
        print("compressing " + fileName + " using PNG")
