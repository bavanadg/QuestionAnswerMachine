import pytest

from QuestionAnswerMachine.consoleapp import ConsoleApp
from QuestionAnswerMachine.question_answer_manager import AnsweringManager


@pytest.fixture
def mock_object():
    am = AnsweringManager(ConsoleApp)
    return AnsweringManager(am)


@pytest.fixture
def scenario1(mock_object):
    mock_object.question_answer_manager("Are you going to work?")


def test_greetUser(mock_object):
    mock_input = "Hello"
    result = mock_object.greetUser()
    assert (result, "Hello")


def test_displayResult2(mock_object):
    result = mock_object.displayResult('How are you?', 'Very good')
    assert (result, "I think that you asked ","\'"," How are you? ","\'"" and conclude that the answer is  ","\'"," Very good ")


