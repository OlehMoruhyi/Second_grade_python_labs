from os.path import isfile
from re import findall


class Text:
    def __init__(self, name):
        if not isinstance(name, str) or not isfile(name):
            raise Exception
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not isfile(name):
            raise Exception
        self.__name = name

    def symbols(self):
        lens = 0
        f = open(self.name)
        for line in f:
            lens += len(line)
        f.close()
        return lens

    def words(self):
        lens = 0
        f = open(self.name)
        for line in f:
            lens += len(findall('[`\-\w]+', line))
        f.close()
        return lens

    def sentences(self):
        counter = 0
        f = open(self.name)
        ind = False
        ch = f.read(1)
        while ch != '':
            if ind and (ch in ('!', '.', '?')):
                ind = False
            elif not ind and ch not in ('!', '.', '?'):
                ind = True
                counter += 1
            ch = f.read(1)
        return counter


obj = Text('text.txt')
print('sentences: ', obj.sentences())
print('words: ', obj.words())
print('letters: ', obj.symbols())
