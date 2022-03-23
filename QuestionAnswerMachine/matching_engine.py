import re


class MatchingEngine:

    # Questions and answers from the catalogue is to be passed through lists ques and ans respectively
    def __init__(self, ques=[], ans=[]):
        self.__questions = ques
        self.__answers = ans

    # Cleans a string from punctuations, replaced with a white space, and returns a list
    # of words
    def cleanedStringList(self, aQuestion):
        list_out = []
        aQuestion = re.sub("[ ,.,?,']", " ", aQuestion)
        list_out = aQuestion.lower().split()
        return list_out

    # The question asked by the user is split in to words and loaded in to a list 'asked_question_word'
    # and question accessed from the question answer catalogue is split in to words and loaded into
    # ques_catalogue_word
    def jaccard_similarity(self, askedQuestionList, aQuestionCatalogueList):
        score = 0
        intersection = len(list(set(askedQuestionList).intersection(aQuestionCatalogueList)))
        union = (len(askedQuestionList) + len(aQuestionCatalogueList)) - intersection
        score = round(float(intersection) / union, 3)
        return score

    # Uses the question entered by the user to calculate the Jaccard Similarity Score to
    # find the closest match for the question in the catalogue
    def question_answer_match(self, userQuestion):
        aQuestionCatalogue = []
        asked_question = []
        asked_question = self.cleanedStringList(userQuestion)
        index = 1
        pos = 1
        max_score = 0

        for pos in range(len(self.__questions)):
            aQuestion = self.__questions[pos]
            aQuestionCatalogue = self.cleanedStringList(aQuestion)
            score = self.jaccard_similarity(asked_question, aQuestionCatalogue)
            if score > max_score:
                max_score = score
                index = pos
            pos = pos + 1

        if max_score > 0.0:
            questionMatched = self.__questions[index]
            answerMatched = self.__answers[index]
        else:
            questionMatched = ""
            answerMatched = ""
        # returns the matched question and answer from the catalogue
        return questionMatched, answerMatched

