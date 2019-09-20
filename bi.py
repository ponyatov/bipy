import os,sys

try:
    SRC = open(sys.argv[1],'rb').read()
except IndexError:
    SRC = open(sys.argv[0],'rb').read()

import ply.lex  as lex
import ply.yacc as yacc
