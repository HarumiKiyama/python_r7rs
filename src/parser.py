from ply.yacc import yacc
from ast import Add, Car, Cdr, Cond, Cons, Div, Mul, Sub
from lexer import tokens  # noqa

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
    class_dict = {"ADD": Add, "SUB": Sub, "MUL": Mul, "DIV": Div}
    p[0] = class_dict[p[2].type](p[3], p[4])


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


def p_expression_quote(p):
    """
    expression : quote
    """
    p[0] = p[1]


def p_expression_pair(p):
    """
    expression : pair
    """
    p[0] = p[1]


def p_pair(p):
    """
    pair : LPAREN CONS expression expression RPAREN
    """
    p[0] = (p[2], p[3], p[4])


def p_expression_define(p):
    """
    expression : LPAREN DEFINE NAME expression RPAREN
    """
    p[0] = ("define", p[3], p[4])


def p_expression_lambda(p):
    """
    expression : LPAREN LAMBDA LPAREN args RPAREN expression RPAREN
    """
    p[0] = ("lambda", p[4], p[6])


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
    args : args NAME
    """
    p[0] = p[1] + [p[2]]


def p_args_single(p):
    """
    args : NAME
    """
    p[0] = [p[1]]


def p_expression_item(p):
    """
    expression : item
    """
    p[0] = p[1]


def p_item_number(p):
    """
    item : NUMBER
    """
    p[0] = ("number", p[1])


def p_item_name(p):
    """
    item : NAME
    """
    p[0] = ("name", p[1])


def p_item_nil(p):
    """
    item : NIL
    """
    p[0] = Nil


def p_error(p):
    print(f"Syntax error at {p.value!r}")


# Build the parser
parser = yacc()
