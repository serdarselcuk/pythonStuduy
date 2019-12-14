mors_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabet = [ 'a' ,'b'   ,'c'   ,'d'  ,'e','f'   ,'g'  ,'h'   ,'i' ,'j'   ,'k'  ,'l'   ,'m' ,'n' ,'o'  ,'p'   ,'q'   ,'r'  ,'s'  ,'t','u'  ,'v'   ,'w'   ,'x'  ,'y'   ,'z'          ]

words = ["gin", "zen", "gig", "msg"]

trans_tot = []

for i in range(len(words)):
    translate = ''
    for char in words[i] :
        translate = translate + mors_list[alphabet.index(char)]
    trans_tot.append(translate)
set_tr = set(trans_tot)

print(trans_tot)
print(set_tr)