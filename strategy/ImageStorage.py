from Compressor import Compressor, JPEGCompressor, PNGCompressor
from Filter import Filter, BlackAndWhiteFilter, SepalFilter


class ImageStorage:

    def __init__(self):
        self.__compressor = JPEGCompressor()
        self.__filter = None

    def store(self, fileName: str) -> None:
        if self.__filter is not None:
            self.__filter.apply(fileName)

        self.__compressor.compress(fileName)

    def set_compressor(self, compressor: Compressor) -> None:
        self.__compressor = compressor

    def set_filter(self, filter: Filter) -> None:
        self.__filter = filter
