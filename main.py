from __future__ import annotations

from abc import ABC, abstractmethod

from block import Block


class Node:
    def __init__(self, block: Block, idx: tuple[int, ...]):
        self.block = block
        self.idx = idx

class Field:



    def __init__(self, *args):
        self.field = self.__construct_field(*args)

    @classmethod
    def __construct_field(cls, *args):
        if len(args) == 1:
            return [Node(block=None, idx=) for _ in range(args[0])]
        return [cls.__construct_field(*args[:-1]) for _ in range(args[-1])]

    def _real_construct(self, *args):

    @staticmethod
    def empty(self, *args) -> Field:
        return Field(*args)

    def place_block(self):
        ...




class BlocksVariations:
    pass


class Generator(ABC):

    @abstractmethod
    def generate(self, field: Field, blocks: BlocksVariations) -> None:
        ...


    def dfs(self):
        ...


class BlockGenerator(Generator):

    def __init__(self):
        self.q = []

    def generate(self, field: Field):
        for i in field.get
        pass


def startapp():
    N = 10
    M = 10

    f: Field = Field.empty(N,M)

    g: Generator = BlockGenerator()

    try:
        g.generate(f)
    except:
        raise Exception()


if __name__ == "__main__":
    startapp()