import pytest

from src.lexer import lexer
from src.parser import parser


@pytest.fixture
def lexer_stub():
    yield lexer


@pytest.fixture
def parser_stub():
    yield parser
