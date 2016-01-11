#!/usr/bin/python3


from abc import ABCMeta, abstractmethod


class AbstractContainer(metaclass=ABCMeta):
    """Should be inherited from AbstractFile"""
    @abstractmethod
    def __init__(self, filename):
        pass

    @abstractmethod
    def container_space(self):
        """Returns number of bytes, which can be hide here."""
        pass

    @abstractmethod
    def hide(self, bytes_data):
        """Hides data in himself."""
        pass

    @abstractmethod
    def reveal(self, num):
        """Reveals 'num' of bytes."""
        pass


class AbstractFile(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, filename):
        pass

    @abstractmethod
    def get_size(self):
        """Returns a size of file."""
        pass

    @abstractmethod
    def print_info(self):
        """Prints interior info of file."""
        pass

    @abstractmethod
    def save_to_disk(self, filename):
        """Writes self to disk"""
        pass


def main():
    pass


if __name__ == '__main__':
    main()
