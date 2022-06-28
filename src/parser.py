from ply.yacc import yacc

from src.ast import Add, Car, Cdr, Cond, Cons, Div, Mul, Sub, Lambda, Define, Number, Nil, Name, Apply
from src.lexer import tokens  # noqa


# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression_bin_operate(p):
    """
    expression : LPAREN ADD expression expression RPAREN
               | LPAREN SUB expression expression RPAREN
               | LPAREN MUL expression expression RPAREN
               | LPAREN DIV expression expression RPAREN
               | LPAREN EQ_Q expression expression RPAREN
    """
    class_dict = {"+": Add, "-": Sub, "*": Mul, "/": Div}
    p[0] = class_dict[p[2]](p[3], p[4])


def p_expression_equal(p):
    """
    expression : lambda
               | quote
               | item
               | pair
               | apply
               | define
    """
    p[0] = p[1]


def p_expression_single_operate(p):
    """
    expression : LPAREN CDR pair RPAREN
               | LPAREN CDR quote RPAREN
               | LPAREN COND condition RPAREN
               | LPAREN CAR pair RPAREN
               | LPAREN CAR quote RPAREN
               | LPAREN ATOM_Q expression RPAREN
    """
    class_dict = {"CDR": Cdr, "CAR": Car, "COND": Cond}
    p[0] = class_dict[p[2].type](p[3])


def p_quote(p):
    """
    quote : LPAREN QUOTE quote_items RPAREN
    """
    p[0] = p[3]


def p_quote_items(p):
    """
    quote_items : expression quote_items
    """
    p[0] = Cons(p[1], p[2])


def p_quote_item(p):
    """
    quote_items : expression
    """
    p[0] = Cons(p[1], Nil)


def p_pair(p):
    """
    pair : LPAREN CONS expression expression RPAREN
    """
    p[0] = (p[2], p[3], p[4])


def p_define(p):
    """
    define : LPAREN DEFINE NAME expression RPAREN
    """
    p[0] = Define(p[3], p[4])


def p_lambda(p):
    """
    lambda : LPAREN LAMBDA LPAREN args RPAREN expression RPAREN
    """
    p[0] = Lambda(p[4], p[6])


def p_apply(p):
    """
    apply : LPAREN lambda args RPAREN
          | LPAREN NAME args RPAREN
    """
    p[0] = Apply(p[2], p[3])


def p_condition_single(p):
    """
    condition : LPAREN  LPAREN expression expression RPAREN RPAREN
    """
    p[0] = [(p[3], p[4])]


def p_condition_multi(p):
    """
    condition : LPAREN expression expression condition RPAREN
    """
    p[3].append((p[2], p[3]))
    p[0] = p[3]


def p_args_multi(p):
    """
    args : args item
    """
    p[0] = p[1] + [p[2]]


def p_args_single(p):
    """
    args : item
    """
    p[0] = [p[1]]


def p_item_number(p):
    """
    item : NUMBER
    """
    p[0] = Number(p[1])


def p_item_name(p):
    """
    item : NAME
    """
    p[0] = Name(p[1])


def p_item_nil(p):
    """
    item : NIL
    """
    p[0] = Nil()


def p_error(p):
    print(f"Syntax error at {p.value!r}")


# Build the parser
parser = yacc()
