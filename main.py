# função: tipo nome(args,...)
# atrib: tipo nome=valor;
from dataclasses import replace
import os

def get_libs(lines):
    pass

def format(lines):
    while '' in lines:
        lines.remove('')
    return lines

def rmv_comments(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')

def rmv_enter(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return format(lines)

def read(file):
    os.chdir(os.path.dirname(__file__))
    with open(file) as f:
        lines = f.readlines()
    return lines

lines = read('teste.c')
lines = rmv_enter(lines)
print(lines)


