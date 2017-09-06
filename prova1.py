import os.path
import shutil
from os.path import exists
from os.path import isfile

# print os.listdir('./')

if(os.path.exists('lista.lst')):
    # controlla gli atlri
    if(os.path.exists('error')):
        print "error esiste"
        # la cartella esiste
    else:
        print "creazione error"
        os.mkdir('error')
        # crea la cartella error
        if(os.path.exists('ok')):
            # la cartella esiste
            pass
        else:
            # crea la cartella ok
            os.mkdir('ok')
else:
    # stop
    pass
# fino a qui tutto bene
'''
    input = open("lista.lst", "r")
    output = open("ok.lst", "r")
    trash = open("error.lst", "w")
'''

input = os.listdir('./')
input2 = open('lista.lst', 'rw')
for linea in input2.readlines():
    linea = linea.strip()
    if os.path.isfile(linea):
        # print 'file :' + linea
        shutil.move('./' + linea, './ok')
        # print "moveok"


input = os.listdir('./')

for linea in input:
    if linea == "lista.lst" or linea == "ok" or linea == "error" or linea == "prova1.py":
        pass
    else:
        print (os.path.join('./', linea))
        shutil.move('./' + linea, './error')
        # shutil.move(os.path.join('./', linea), './error')
        print "moverror"




# for linea in input2.split(str=";", num=string.count(input2))
