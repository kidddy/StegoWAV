#!/usr/bin/python3


class AbstractContainer:
    """Should be inherited from AbstractFile"""
    def __init__(self, filename):
        raise NotImplementedError("Need to rewrite method.")

    def container_space(self):
        """Returns number of bytes, which can be hide here."""
        raise NotImplementedError("Need to rewrite method.")

    def hide(self, bytes_data):
        """Hides data in himself."""
        raise NotImplementedError("Need to rewrite method.")

    def reveal(self, num):
        """Reveals 'num' of bytes."""


class AbstractFile:
    def __init__(self, filename):
        raise NotImplementedError("Need to rewrite method.")

    def get_size(self):
        """Returns a size of file."""
        raise NotImplementedError("Need to rewrite method.")

    def print_info(self):
        """Prints interior info of file."""
        raise NotImplementedError("Need to rewrite method.")

    def saveToDisk(self, filename):
        """Writes self to disk"""
        raise NotImplementedError("Need to rewrite method.")



def main():
    pass


if __name__ == '__main__':
    main()
