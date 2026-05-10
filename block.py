from __future__ import annotations

from abc import ABC,abstractmethod
from enum import Enum


class Direction(Enum):
    right = "right"
    left = "left"
    up = "up"
    down = "down"


class Block(ABC):
    ...

    def __init__(self, label="?"):
        self.label = label

    @abstractmethod
    def add_link(self, other: Block, direction: Direction) -> None:
        ...

    @abstractmethod
    def clear(self):
        ...
