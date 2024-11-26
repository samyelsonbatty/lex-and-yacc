import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


lexer.input("3 + 4 * 5")

# lexer clone
lookahead_lexer = lexer.clone()

# Analyze a portion of text using cloning
# Read all numbers using the cloned version
count_numbers = 0
while True:
    tok = lookahead_lexer.token()
    if not tok:
        break
    if tok.type == 'NUMBER':
        count_numbers += 1

print("Number of numbers in the expression:", count_numbers)
if count_numbers % 2 == 1:
    print("The expression has an odd number of numbers.")
else:
    print("The expression has an even number of numbers.")

