import json


class QuestionCatalogueAccess:

    # This class manages 'questions_catalogue_store' or the 'faq.json'
    def __init__(self, ques=[], ans=[]):
        self.__questions = ques
        self.__answers = ans

    # This method opens and loads json data from 'faq.json' in to question and
    # answer lists
    def openFaqJson(self, fileName):
        try:
            with open(fileName, "r") as file:
                data = json.load(file)
                for x in data:
                    self.__questions.append(x['question'])
                    self.__answers.append(x['answer'])
        except IOError as e:
            print("An error occurred while opening faq.json file: ", e)
            exit()
        finally:
            file.close()
        return self.__questions, self.__answers
