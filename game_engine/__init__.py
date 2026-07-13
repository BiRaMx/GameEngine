"""
Игровой фреймворк.

Модули:
 - grid - объекты для работы с различными сетками
"""

from grid import Grid

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("game_engine")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ['Grid']

print(f"BiRaM Game Framework. Version: {__version__}.")

# TMP: чтобы установить проект: pip install -e . из директории game_engine