#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class OrderInspector(metaclass=ABCMeta):
    def __init__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n should be int and n >= 0.")
        self._limit = n
        self._count = 0

    @abstractmethod
    def next(self):
        pass

    def restart(self):
        self._count = 0


class LinearOrderInspector(OrderInspector):
    def __init__(self, n):
        OrderInspector.__init__(self, n)

    def next(self):
        if self._count == self._limit:
            return -1
        self._count += 1
        return self._count - 1


class ReversedLinearOrderInspector(OrderInspector):
    def __init__(self, n):
        OrderInspector.__init__(self, n)

    def next(self):
        if self._count == self._limit:
            return -1
        self._count += 1
        return self._limit - (self._count - 1)


class WaveOrderInspector(OrderInspector):
    def __init__(self, n):
        OrderInspector.__init__(self, n)

    def next(self):
        if self._count == self._limit:
            return -1
        flag = 0
        if self._count % 2 == 1:
            flag = 1
        self._count += 1
        return self._limit * flag + self._count * (-1)**flag


ORDER_INSPECTORS = dict()
ORDER_INSPECTORS[0] = LinearOrderInspector
ORDER_INSPECTORS[1] = ReversedLinearOrderInspector
ORDER_INSPECTORS[2] = WaveOrderInspector


def main():
    pass


if __name__ == '__main__':
    main()


