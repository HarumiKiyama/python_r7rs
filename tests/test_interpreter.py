import logging


def test_interpreter_operate(parser_stub):
    ast = parser_stub.parse('(+ 1 2)')
    t = ast.eval()
    assert t == 3


def test_interpreter_lambda(parser_stub):
    s = '''((lambda (a b) (+ a b)) 1 2)'''
    ast = parser_stub.parse(s)
    assert ast.eval() == 3
