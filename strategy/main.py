from ImageStorage import ImageStorage
import Compressor as cmp
import Filter as flt


def main() -> None:

    image_storage = ImageStorage()

    image_storage.store("selfie 1")

    filter = flt.SepalFilter()
    image_storage.set_filter(filter)

    image_storage.store("selfie 2")

    compressor = cmp.PNGCompressor()
    image_storage.set_compressor(compressor)

    image_storage.store("selfie 3")

    return


if __name__ == '__main__':
    main()
