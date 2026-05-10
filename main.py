from __future__ import annotations

from abc import ABC, abstractmethod

from block import Block


class Node:
    def __init__(self, block: Block, idx: tuple[int, ...]):
        self.block = block
        self.idx = idx

    def clear(self):
        self.block.clear()


class Field:

    def __init__(self, *args):
        self.field = self._real_construct(*args)
        self.depth = len(args)

    @classmethod
    def __construct_field(cls, *args, idx: list[int], depth=0):
        res = []
        if len(args) == 1:
            for i in range(args[0]):
                res.append(Node(block=None, idx=idx))
                idx[depth] += 1
            idx[depth] = 0
            return res

        for i in range(args[-1]):
            res.append(cls.__construct_field(*args[:-1], idx=idx, depth=depth + 1))
            idx[depth] += 1
        idx[depth] = 0
        return res

    def _real_construct(self, *args):
        idx = [0] * len(args)
        return self.__construct_field(*args, idx=idx, depth=0)

    @staticmethod
    def empty(*args) -> Field:
        return Field(*args)

    def place_block(self, idx: tuple[int, ...]):
        ...

    def delete_block(self, idx: tuple[int, ...]):
        ...

    def get_by_idx(self, idx: list[int], lst=None) -> Node:
        if lst is None:
            lst = self.field
        if len(idx) == 1:
            return lst[idx[0]]
        return self.get_by_idx(idx=idx[1:], lst=lst[idx[0]])


class BlocksVariations:
    pass


class Generator(ABC):

    def __init__(self):
        ...

    @abstractmethod
    def generate(self, field: Field, blocks: BlocksVariations) -> None:
        ...


class PriorityQueueSet:

    def __init__(self):
        self.q = []

    def put(self, other):
        ...

    def pop(self):
        ...

    def poll(self):
        ...


class BlockGenerator(Generator):

    def __init__(self):
        super().__init__()
        self._field: Field = None
        self.__seed = 67
        self._q = PriorityQueueSet()

    @abstractmethod
    def generate(self, field: Field, blocks: BlocksVariations) -> None:
        self._field = field
        self.scan()
        self.dfs(idx=[0] * field.depth)

    def scan(self):
        ...

    def dfs(self, idx: list[int]):
        idx: list[int] = self._q.pop()

        b = self._field.get_by_idx(idx)
        b.

        self._field.get_by_idx(idx).clear()


def startapp():
    N = 10
    M = 10

    f: Field = Field.empty(N, M)

    g: Generator = BlockGenerator()

    try:
        g.generate(f)
    except:
        raise Exception()


if __name__ == "__main__":
    startapp()
