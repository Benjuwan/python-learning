from abc import *

class Command(ABC):
    @abstractmethod
    def run(self, text):
        pass

class Append(Command):
    def __init__(self, text):
        self.text = text

    def run(self, text):
        return text+self.text

class Insert(Command):
    def __init__(self, index, text):
        self.index = index
        self.text = text

    def run(self, text):
        i = self.index
        return text[:i]+self.text+text[i:]

c = [Append('th'), Insert(0, 'py'), Append('on')]
s = ''
for x in c:
    s = x.run(s)
print(s)
