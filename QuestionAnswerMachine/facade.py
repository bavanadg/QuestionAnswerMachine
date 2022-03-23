from __future__ import annotations
from consoleapp import ConsoleApp
from question_answer_manager import AnsweringManager
from matching_engine import MatchingEngine
from question_catalogue_access import QuestionCatalogueAccess
from question_log_access import QuestionLog


class Facade:

    def __init__(self,qaManager, mEngine, qLog, qCatalogue):
        self.__qamanager = qaManager
        self.__mengine = mEngine
        self.__qlog = qLog
        self.__qcatalogue = qCatalogue

    def runChatBot(self):
        questions = []
        answers = []
        qa_manager = AnsweringManager("Please enter a question, and press the ENTER key: ")
        qa_manager.greetUser()
        self.__qcatalogue = QuestionCatalogueAccess(questions, answers)
        questions, answers = self.__qcatalogue.openFaqJson("faq.json")
        self.__mengine = MatchingEngine(questions, answers)
        userQuestion = qa_manager.accquireUserInput()
        while userQuestion != "":
            # write the question to the asked_questions_log.txt file
            self.__qlog = QuestionLog(userQuestion, 'asked_questions_log.txt')
            self.__qlog.writeAskedQuestion()


            # q_matched and a_matched refers to question and answer matched respectively from catalogue
            # of questions with user asked question
            q_matched, a_matched = self.__mengine.question_answer_match(userQuestion)
            qa_manager.displayResult(q_matched, a_matched)
            userQuestion = qa_manager.accquireUserInput()

        if userQuestion == "":
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    facade = Facade(AnsweringManager,MatchingEngine,QuestionLog,QuestionCatalogueAccess)
    facade.runChatBot()
