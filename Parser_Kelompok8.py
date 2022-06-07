#Program Parser

#Kelompok 8

#Reza Donsika Putra (1301201403)
#Albertus Ivan Martino (1301204114)
#Regita Indri Cahyani (1301204083)

# input example
sentence = input("Input Sentence : ")
tokens = sentence.lower().split()
tokens.append('EOS')

# Symbols definition
non_terminals = ['S', 'SU', 'VB', 'OB']
terminals = ['mother', 'father', 'eating', 'wearing', 'playing', 'jacket', 'jeans', 'noodle', 'sushi', 'game']

# parse table definition
parse_table = {}

parse_table[('S', 'father')] = ['SU', 'VB', 'OB']
parse_table[('S', 'mother')] = ['SU', 'VB', 'OB']
parse_table[('S', 'eating')] = ['error']
parse_table[('S', 'wearing')] = ['error']
parse_table[('S', 'playing')] = ['error']
parse_table[('S', 'jacket')] = ['error']
parse_table[('S', 'jeans')] = ['error']
parse_table[('S', 'noodle')] = ['error']
parse_table[('S', 'game')] = ['error']
parse_table[('S', 'sushi')] = ['error']
parse_table[('S', 'EOS')] = ['error']


parse_table[('SU', 'father')] = ['father']
parse_table[('SU', 'mother')] = ['mother']
parse_table[('SU', 'eating')] = ['error']
parse_table[('SU', 'wearing')] = ['error']
parse_table[('SU', 'playing')] = ['error']
parse_table[('SU', 'jacket')] = ['error']
parse_table[('SU', 'jeans')] = ['error']
parse_table[('SU', 'noodle')] = ['error']
parse_table[('SU', 'game')] = ['error']
parse_table[('SU', 'sushi')] = ['error']
parse_table[('SU', 'EOS')] = ['error']

parse_table[('VB', 'father')] = ['error']
parse_table[('VB', 'mother')] = ['error']
parse_table[('VB', 'eating')] = ['eating']
parse_table[('VB', 'wearing')] = ['wearing']
parse_table[('VB', 'playing')] = ['playing']
parse_table[('VB', 'jacket')] = ['error']
parse_table[('VB', 'jeans')] = ['error']
parse_table[('VB', 'noodle')] = ['error']
parse_table[('VB', 'game')] = ['error']
parse_table[('VB', 'sushi')] = ['error']
parse_table[('VB', 'EOS')] = ['error']

parse_table[('OB', 'father')] = ['error']
parse_table[('OB', 'mother')] = ['error']
parse_table[('OB', 'eating')] = ['error']
parse_table[('OB', 'wearing')] = ['error']
parse_table[('OB', 'playing')] = ['error']
parse_table[('OB', 'jacket')] = ['error']
parse_table[('OB', 'jeans')] = ['error']
parse_table[('OB', 'noodle')] = ['noodle']
parse_table[('OB', 'game')] = ['game']
parse_table[('OB', 'sushi')] = ['sushi']
parse_table[('OB', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input remotherng initialization
idx_token = 0
symbol = tokens[idx_token]

#parsing process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top==symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack: ', stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack:', stack)
    print()
    
#conclusion
print()
if symbol == 'EOS' and len(stack)==0:
    print('input string', sentence, 'diterima, sesuai Grammar')
else:
    print('Error, input string: ', sentence, ', tidak diterima, tidak sesuai Grammar')
