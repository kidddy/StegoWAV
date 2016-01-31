#!/usr/bin/python3


class Enumerator:
    def __init__(self, sequence):
        self._body = sequence
        self._iter = iter(self._body)
        self._pos = 0

    def seek(self, position):
        self._pos = position
        self._iter = iter(self._body)
        step = 0
        try:
            while step != self._pos:
                next(self._iter)
                step += 1
        except StopIteration:
            pass

    def get_size(self):
        return len(self._body)

    def tell(self):
        return self._pos

    def read(self, num=-1):
        if num == -1:
            num = self.get_size() - self._pos
        step = 0
        result = []
        try:
            while step != num:
                result.append(next(self._iter))
                step += 1
        except StopIteration:
            pass
        self._pos += num
        return result


def main():
    pass


if __name__ == '__main__':
    main()
