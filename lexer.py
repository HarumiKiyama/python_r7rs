from ply.lex import lex

reserved = {
    'define':'DEFINE',
    'if' : 'IF',
    'else': 'ELSE',
    'for' : 'FOR',
    'while': 'WHILE',
    'lambda' : 'LAMBDA',
    'cond': 'COND',
    'quote': 'QUOTE',

}

# All tokens must be named in advance.
tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
           'NAME', 'NUMBER'] + list(reserved.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

