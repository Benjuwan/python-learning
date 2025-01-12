from abc import *

class Command(ABC):
    @abstractmethod
    def run(self, text):
        pass
