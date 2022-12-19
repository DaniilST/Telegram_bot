from typing import Tuple

from aiogram import types


def create_media(paths: Tuple[str, str, str, str]) -> types.MediaGroup:
    media = types.MediaGroup()

    media.attach_photo(types.InputFile(paths[3]), caption='Гисторграмма среднего распределения яркости')
    media.attach_photo(types.InputFile(paths[0]), caption='Гистограмма канала R')
    media.attach_photo(types.InputFile(paths[1]), caption='Гистограмма канала B')
    media.attach_photo(types.InputFile(paths[2]), caption='Гистограмма канала G')
    return media
