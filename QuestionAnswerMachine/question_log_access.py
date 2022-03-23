class QuestionLog:

    # This class manages 'asked_questions_store'
    def __init__(self, quest, questionFileName):
        self.__question = quest + "\n"
        self.__questionsFileName = questionFileName

    # This method writes user entered question in to 'asked_questions_store'
    def writeAskedQuestion(self):
        try:
            with open(self.__questionsFileName, "a") as f:
                f.write(self.__question)
                f.close()
        except IOError as e:
            print("An error occurred during writing to the asked_questions.txt file: ", e)
