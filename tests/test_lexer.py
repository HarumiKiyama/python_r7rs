def test_lexer_define(lexer_stub):
    lexer_stub.input("(define t (+ 1 2))")
    tokens = [i.type for i in lexer_stub]
    assert tokens == [
        "LPAREN",
        "DEFINE",
        "NAME",
        "LPAREN",
        "PLUS",
        "NUMBER",
        "NUMBER",
        "RPAREN",
        "RPAREN",
    ]


def test_lexer_quote(lexer_stub):
    lexer_stub.input("(cons 1 2)")
    tokens = [i.type for i in lexer_stub]
    assert tokens == [
        "LPAREN",
        'CONS',
        "NUMBER",
        "NUMBER",
        "RPAREN",
    ]


def test_lexer_define_lambda(lexer_stub):
    lexer_stub.input("(define tf (lambda (x) (+ x 1)))")
    tokens = [i.type for i in lexer_stub]
    assert tokens == [
        "LPAREN",
        "DEFINE",
        "NAME",
        "LPAREN",
        "LAMBDA",
        "LPAREN",
        "NAME",
        "RPAREN",
        "LPAREN",
        "PLUS",
        "NAME",
        "NUMBER",
        "RPAREN",
        "RPAREN",
        "RPAREN",
    ]
