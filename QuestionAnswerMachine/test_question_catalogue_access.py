import pytest

from question_catalogue_access import QuestionCatalogueAccess


@pytest.fixture
def mock_object():
    qca = QuestionCatalogueAccess()
    return qca


@pytest.fixture
def scenario1(mock_object):
    mock_object.question_answer_manager("Are you going to work?")


def test_openFaqJson(mock_object):
    result = mock_object.openFaqJson('faq.json')
    assert type(result) is tuple

