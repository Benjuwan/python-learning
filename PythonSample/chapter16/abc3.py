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
