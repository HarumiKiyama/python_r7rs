import pytest
from lexer import lexer
from parser import parser


@pytest.fixture
def lexer_stub():
    yield lexer

@pytest.fixture
def parser_stub():
    yield parser
