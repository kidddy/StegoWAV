#!/usr/bin/python3


from abstracts import AbstractContainer
from .wavFile import WavFile



class WavContainer(AbstractContainer, WavFile):
    def __init__(self, filename):
        WavFile.__init__(self, filename)

    def container_space(self):
        return (
            self.chunks['data'].get_size() //
            self.chunks['fmt '].blockAlign //
            8
        )

    def hide(self):
        pass
        #TODO

    def reveal(self):
        pass
        #TODO



def main():
    pass

if __name__ == '__main__':
    main()
