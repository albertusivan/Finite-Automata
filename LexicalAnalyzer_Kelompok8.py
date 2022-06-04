#Program Lexical Analyzer

#Kelompok 8

#Reza Donsika Putra (1301201403)
#Albertus Ivan Martino (1301204114)
#Regita Indri Cahyani (1301204083 

import string

#input example
sentence = input("Input Sentence : ")
input_string = sentence.lower()+'#'

#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
              'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
              'q21','q22','q23','q24','q25','q26','q27','q28','q29','q30',
              'q31','q32','q33','q34','q35','q36','q37','q38','q39']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

#spaces before input string
transition_table[('q0',' ')] = 'q0'

#transition for new token
transition_table[('q39','m')] = 'q1'
transition_table[('q39','f')] = 'q2'
transition_table[('q39','e')] = 'q7'
transition_table[('q39','w')] = 'q9'
transition_table[('q39','p')] = 'q15'
transition_table[('q39','j')] = 'q18'
transition_table[('q39','n')] = 'q26'
transition_table[('q39','s')] = 'q31'
transition_table[('q39','g')] = 'q35'

#update the transition table for the following token : mother
transition_table[('q0','m')] = 'q1'
transition_table[('q1','o')] = 'q3'
transition_table[('q3','t')] = 'q4'
transition_table[('q4','h')] = 'q5'
transition_table[('q5','e')] = 'q6'
transition_table[('q6','r')] = 'q38'
transition_table[('q38',' ')] = 'q39'

#update the transition table for the following token : father
transition_table[('q0','f')] = 'q2'
transition_table[('q2','a')] = 'q3'
transition_table[('q3','t')] = 'q4'
transition_table[('q4','h')] = 'q5'
transition_table[('q5','e')] = 'q6'
transition_table[('q6','r')] = 'q38'
transition_table[('q38',' ')] = 'q39'

#update the transition table for the following token : eating
transition_table[('q0','e')] = 'q7'
transition_table[('q7','a')] = 'q8'
transition_table[('q8','t')] = 'q12'
transition_table[('q12','i')] = 'q13'
transition_table[('q13','n')] = 'q14'
transition_table[('q14','g')] = 'q38'
transition_table[('q38',' ')] = 'q39'

#update the transition table for the following token : wearing
transition_table[('q0','w')] = 'q9'
transition_table[('q9','e')] = 'q10'
transition_table[('q10','a')] = 'q11'
transition_table[('q11','r')] = 'q12'
transition_table[('q12','i')] = 'q13'
transition_table[('q13','n')] = 'q14'
transition_table[('q14','g')] = 'q38'
transition_table[('q38',' ')] = 'q39'

#update the transition table for the following token : playing
transition_table[('q0','p')] = 'q15'
transition_table[('q15','l')] = 'q16'
transition_table[('q16','a')] = 'q17'
transition_table[('q17','y')] = 'q12'
transition_table[('q12','i')] = 'q13'
transition_table[('q13','n')] = 'q14'
transition_table[('q14','g')] = 'q38'
transition_table[('q38',' ')] = 'q39'

#update the transition table for the following token : jacket
transition_table[('q0','j')] = 'q18'
transition_table[('q18','a')] = 'q19'
transition_table[('q19','c')] = 'q20'
transition_table[('q20','k')] = 'q21'
transition_table[('q21','e')] = 'q22'
transition_table[('q22','t')] = 'q38'
transition_table[('q38','#')] = 'accept'

#update the transition table for the following token : jeans
transition_table[('q0','j')] = 'q18'
transition_table[('q18','e')] = 'q23'
transition_table[('q23','a')] = 'q24'
transition_table[('q24','n')] = 'q25'
transition_table[('q25','s')] = 'q38'
transition_table[('q38','#')] = 'accept'

#update the transition table for the following token : noodle
transition_table[('q0','n')] = 'q26'
transition_table[('q26','o')] = 'q27'
transition_table[('q27','o')] = 'q28'
transition_table[('q28','d')] = 'q29'
transition_table[('q29','l')] = 'q30'
transition_table[('q30','e')] = 'q38'
transition_table[('q38','#')] = 'accept'

#update the transition table for the following token : sushi
transition_table[('q0','s')] = 'q31'
transition_table[('q31','u')] = 'q32'
transition_table[('q32','s')] = 'q33'
transition_table[('q33','h')] = 'q34'
transition_table[('q34','i')] = 'q38'
transition_table[('q38','#')] = 'accept'

#update the transition table for the following token : game
transition_table[('q0','g')] = 'q35'
transition_table[('q35','a')] = 'q36'
transition_table[('q36','m')] = 'q37'
transition_table[('q37','e')] = 'q38'
transition_table[('q38','#')] = 'accept'

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state,current_char)]
    if state == 'q38' :
        print('current token: ',current_token,', valid')
        current_token = ''
    if state == 'error' :
        print('error')
        break
    idx_char = idx_char + 1

#conclusion
if state == 'accept':
  print('semua token di input: ',sentence, ', valid')