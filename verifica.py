import os.path
from os.path import exists
from os.path import isfile


    
print os.listdir('./')

if(os.path.exists('lista.lst')):
    #controlla gli atlri
    if(os.path.exists('error')):
        #la cartella esiste
        pass
    else:
        os.mkdir('error')
        #crea la cartella error
        if(os.path.exists('ok')):
            #la cartella esiste
            pass
        else:
            #crea la cartella ok
            os.mkdir('ok')
else:
    #stop
    pass
#fino a qui tutto bene

    '''    
    input = open("lista.lst", "r")
    for linea in input.readlines():
        #se il file esiste nella directory locale lo sposta in ok
    '''
