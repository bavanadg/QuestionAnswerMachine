from consoleapp import ConsoleApp


class AnsweringManager(ConsoleApp):

    def __init__(self, line):
        super().__init__(line)
        self.__messageLine = line

    def greetUser(self):
        print("Hello, I am a question answering machine bot.\n")

    def accquireUserInput(self):
        question = input("\n"+self.__messageLine)
        return question

    def displayResult(self, matchedQuestion, matchedAnswer):
        if matchedQuestion != "":
            print("I think that you asked ","\"",matchedQuestion,"\"","and conclude that the answer is "
                                                                    ,"\"",matchedAnswer,"\"")
        else:
            print("Question you asked does not match to any questions in the question catalogue")


