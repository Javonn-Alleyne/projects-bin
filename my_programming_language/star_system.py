import ply.lex as lex

# list of tokens
tokens = (
    'LOW_MINUS',
    'LOW',
    'LOW_PLUS',
    'MID_MINUS',
    'MID',
    'MID_PLUS',
    'HIGH_MINUS',
    'HIGH',
    'HIGH_PLUS',
    'PERFECT',
    'MISSING',
    'CRITICAL',
)

# expression rules for the tokens
t_LOW_MINUS     = r'v-'
t_LOW           = r'v'
t_LOW_PLUS      = r'v\+'
t_MID_MINUS     = r'~-'
t_MID           = r'~'
t_MID_PLUS      = r'~\+'
t_HIGH_MINUS    = r'\^-'
t_HIGH          = r'\^'
t_HIGH_PLUS     = r'\^\+'
t_PERFECT       = r'\*'
t_MISSING       = r'\?'
t_CRITICAL      = r'!'

# symbol mapping
SYMBOL_MAP = {
    '0':'v-',   # LOW_MINUS
    '1':'v',    # LOW
    '2':'v+',   # LOW_PLUS
    '3':'~-',   # MID_MINUS
    '4':'~',    # MID
    '5':'~+',   # MID_PLUS
    '6':'^-',   # HIGH_MINUS
    '7':'^',    # HIGH
    '8':'^+',   # HIGH_PLUS
    '9':'*',    # PERFECT
    '?':'?',    # MISSING
    '!':'!',    # CRITICAL
}

# ignore whitespace
t_ignore = ' \t'

# error checking
def t_error(t):
    print("Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# build lexer
# lexer = lex.lex()
# lexer.input("v ^ * v") #lexer test
# for tok in lexer:
#     print(tok)

# build fields
fields = []
while True:
    headings = input("Enter a field heading: ") # input fields
    fields.append(headings)
    
    choice = input("Add another field? (y/n): ").lower()
    if choice != 'y':
        break

# build values
symbols = []
names = []

while True:
    name = input("Enter a Name: ")
    names.append(name)

    name_symbols = [] #keep name and symbol combos
    for i in range(len(fields)): # set baseded on the number of fields craeted
        while True:
            num = input(f"Enter a value for field '{fields[i]}' between(0-9): ")
            if num not in SYMBOL_MAP:
                print("Invalide Number, try again")
                continue
            name_symbols.append(SYMBOL_MAP[str(num)])
            break

    symbols.append(name_symbols)

    choice = input("Add another Name? (y/n): ").lower()
    if choice != 'y':
        break

f_result = '{<' + '>|<'.join(fields) + '>}'
print(f"fields: {f_result}")

for name, name_symbols in zip(names, symbols): #combine name with symbols
    s_result = '[ ' + ' | '.join(name_symbols) + ' ]'
    print(f"{name}: {s_result}")

# export results to a file
filename = input("Enter a filename to save (default: results.txt): ") or "results.txt"
with open(filename,'w') as file:
    file.write(f"fields: {f_result} + '\n'")
    for name, name_symbols in zip(names, symbols):
        s_result = '[ ' + ' | '.join(name_symbols) + ' ]'
        file.write(f"{name}: {s_result}\n")
print(f"{filename}, successfully exported!")


