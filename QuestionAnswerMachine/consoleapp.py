from abc import ABC, abstractmethod


class ConsoleApp(ABC):

    def __init__(self,message):
        self.__messageLine1 = message

    @property
    @abstractmethod
    def accquireUserInput(self):
        # abstract method to support MS DOS/Mac/Linux
        pass

    @abstractmethod
    # displays the system response
    def displayResult(self, inResult, outResult):
        pass;