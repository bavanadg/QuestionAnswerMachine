from unittest.mock import Mock
import pytest

from matching_engine import MatchingEngine


@pytest.fixture
def mockObject():
    qca = MatchingEngine()
    return qca


@pytest.fixture
def scenario1(mockObject):
    mockObject.question_answer_manager("Are you going to work?")


def test_cleanedStringList(mockObject):
    mock_input = "abc.?"
    expected = "abc"
    result = mockObject.cleanedStringList(mock_input)
    assert (result, "abc")


def test_jaccard_similarity(mockObject):
    mock_input1 = "Who is the prime minister of Australia"
    mock_input2 = "Who is the"
    expected = "0.6"
    result = mockObject.jaccard_similarity(mock_input1, mock_input2)
    assert (result, "0.6")


def test_question_answer_match(mockObject):
    mock_input1 = "abc?"
    expected = 1
    result = mockObject.question_answer_match(mock_input1)
    assert (result, 1)
