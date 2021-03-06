from abc import ABCMeta, abstractmethod


class AbstractContainer(metaclass=ABCMeta):
    """Should be inherited from AbstractFile"""
    @abstractmethod
    def __init__(self, file_name):
        pass

    @abstractmethod
    def container_space(self):
        """Returns number of bytes, which can be hide here."""
        pass

    @abstractmethod
    def hide(self, bin_data, order_inspector, bad_bits_num=1):
        """Hides data in himself."""
        pass

    @abstractmethod
    def reveal(self, num):
        """Reveals 'num' of bytes."""
        pass


class AbstractFile(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, file_name):
        pass

    @abstractmethod
    def get_size(self):
        """Returns a size of file."""
        pass

    @abstractmethod
    def get_info_text(self):
        """Prints interior info of file."""
        pass

    @abstractmethod
    def save_to_disk(self, file_name):
        """Writes self to disk"""
        pass


def main():
    pass


if __name__ == '__main__':
    main()
