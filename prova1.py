import os.path
import shutil
from os.path import exists
from os.path import isfile

if(os.path.exists('lista.lst')):
    if(os.path.exists('error')):
        pass
    else:
        os.mkdir('error')
    if(os.path.exists('ok')):
        pass
    else:
        os.mkdir('ok')
else:
    pass


input = os.listdir('./')
input2 = open('lista.lst', 'rw')
for linea in input2.readlines():
    linea = linea.strip()
    if os.path.isfile(linea):
        shutil.move('./' + linea, './ok')


input = os.listdir('./')

for linea in input:
    if linea == "lista.lst" or linea == "ok" or linea == "error" or linea == "prova1.py":
        pass
    else:
        shutil.move('./' + linea, './error')