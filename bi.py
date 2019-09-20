import os,sys

try:
    INF = sys.argv[1]
    SRC = open(INF,'rb').read()
except IndexError:
    INF = sys.argv[0]
    SRC = open(INF,'rb').read()

sys.stdout = log = open(INF+'.log','w')
print 'BY:',sys.argv[0]
print 'INF:',INF

import ply.lex  as lex
import ply.yacc as yacc

