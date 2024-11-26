import ply.lex as lex
import logging

logging.basicConfig(filename = 'app.log', level=logging.DEBUG)

tokens = (
    "NUMBER",
    "WORD",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "ASSIGN",
)

t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASSIGN = r'\='


## Define Numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    t.datatype = 'intger'
    logging.debug(f"Token Number : {t.value} at postion {t.lexpos} ")
    return t


## Define Word (String)
def t_WORD(t):
    r'[a-zA-Z]'
    t.value = t.value  # Retain the string value
    t.datatype = 'String'
    logging.debug(f"Token Word: {t.value} at position {t.lexpos}")
    return t

def t_PLUS(t):
    r'\+'
    t.value = '+'
    t.datatype = 'Operator'
    logging.debug(f'Token Operator : {t.value} at postion {t.lexpos}')
    return t


def t_MINUS(t):
    r'\-'
    t.value = '-'
    t.datatype = 'Operator'
    logging.debug(f'Token Operator : {t.value} at postion {t.lexpos}')
    return t


#Error Handling
def t_error(t):
    logging.error(f"Illgal Charcter '{t.value[0]}' at line {t.lineno}, postion {t.lexpos}")
    t.lexer.skip(1)
    

## Ignore
t_ignore = ' \t'


## New Line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
## Build Lexer and Debug Mode
lexer = lex.lex(debug=1)

# DATA
data = '''
(
3 + 4
Hello World 
3 * 20 = 60 - 0
)
'''

lexer.input(data)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"Token : {tok.type}, Value : {tok.value}, Line : {tok.lineno}, postion : {tok.lexpos}, Datatype : {getattr(tok, 'datatype', 'N/A')}")
    

for token in lexer:
    logging.info(f'Token : {token}')
