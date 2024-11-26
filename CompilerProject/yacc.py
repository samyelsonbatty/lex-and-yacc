import ply.yacc as yacc
import logging

# Import the tokens from the lexer
from app import tokens

# Enable logging for debugging
logging.basicConfig(filename='app.parser', level=logging.DEBUG)

# Precedence rules to resolve ambiguity in expressions
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Grammar rules

# Start symbol
def p_statement_expr(p):
    '''statement : expression'''
    logging.info(f"Parsed expression: {p[1]}")
    p[0] = p[1]

def p_statement_assign(p):
    '''statement : WORD ASSIGN expression'''
    logging.info(f"Assignment: {p[1]} = {p[3]}")
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    logging.info(f"Binary operation: {p[2]} with {p[1]} and {p[3]}")
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_word(p):
    '''expression : WORD'''
    p[0] = p[1]

# Error rule
def p_error(p):
    if p:
        logging.error(f"Syntax error at token {p.value!r}, line {p.lineno}")
        print(f"Syntax error at token {p.value!r}, line {p.lineno}")
    else:
        logging.error("Syntax error at EOF")
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test input
data = '''
x = 3 + 4 * (5 - 2)
y = x / 2
z = y - 1
'''

result = parser.parse(data)

print("Parsed result:", result)
