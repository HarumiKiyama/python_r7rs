def test_parser_define(parser_stub):
    ast = parser_stub.parse("(define t 123)")
    assert ast == ("define", "t", ("number", 123))


def test_parser_cons(parser_stub):
    ast = parser_stub.parse("(cons 123 123)")
    assert ast == ("cons", ("number", 123), ("number", 123))


def test_parser_lambda(parser_stub):
    ast = parser_stub.parse("(quote 1 2 3 4)")
    assert ast == (
    "cons", ("number", 1), ("cons", ("number", 2), ("cons", ("number", 3), ("cons", ("number", 4), "nil"))))
