from ply.yacc import yacc
# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression(p):
    '''
    expression : LPAREN PLUS expression expression RPAREN
               | LPAREN MINUS expression expression RPAREN
               | LPAREN TIMES expression expression RPAREN
               | LPAREN DIVIDE expression expression RPAREN
    '''
    p[0] = ('exp', p[2], p[3],  p[4])

def p_expression_define(p):
    '''
    expression : LPAREN DEFINE NAME expression RPAREN
    '''
    p[0] = ('define', p[3], p[4])

def p_expression_lambda(p):
    '''
    expression : LPAREN LAMBDA LPAREN args RPAREN expression RPAREN
    '''
    p[0] = ('lambda', p[4], p[6])

def p_args_1(p):
    '''
    args: args Name
    '''
    p[1].append(p[2])
    p[0] = p[1]

def p_args_2(p):
    '''
    args: Name
    '''
    p[0] = [p[1]]


def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]


def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = ('number', p[1])

def p_factor_name(p):
    '''
    factor : NAME
    '''
    p[0] = ('name', p[1])

def p_error(p):
    print(f'Syntax error at {p.value!r}')

# Build the parser
parser = yacc()


