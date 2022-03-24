from fileinput import filename

import pytest
from _pytest import tmpdir

from QuestionAnswerMachine.consoleapp import ConsoleApp
from QuestionAnswerMachine.question_answer_manager import AnsweringManager
from QuestionAnswerMachine.question_log_access import QuestionLog


@pytest.fixture
def mock_object():
    am = AnsweringManager(ConsoleApp)
    return AnsweringManager(am)


@pytest.fixture
def scenario1(mock_object):
    mock_object.question_answer_manager("Are you going to work?")


def test_writeAskedQuestion(mock_object):
    #file = mock_object.j'quest' and 'questionFileNameoin('output')
    file = mock_object.writeAskedQuestion()
    assert file.write() == 'Are you going to work?'
