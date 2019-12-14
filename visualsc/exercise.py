word=input('*enter a word that starts with "pre": *')
def pre_word():
    
    if word.startswith('pre'):
        
        if word.isalpha():
            return True
        else:
            return False

    else:
        return False

print('your word validation:',pre_word())