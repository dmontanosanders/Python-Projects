# -*- coding: latin_1 -*-
import easygui as eg
import os
import re
import codecs
import sys
from time import localtime, strftime


def main():
    pass

if __name__ == '__main__':
    main()

my = strftime("%m_%Y", localtime())

#try to open attach.txt, return to folder select if fail
x=False
while x==False:
    #Get path to attach.txt
    attch = eg.fileopenbox("","Choose EXPORT attach.txt","K:\\"+my,'.txt')
    pch = re.search('.*(?=attach.txt)',attch,re.IGNORECASE)
    path = pch.group()

    try:
        f = codecs.open(attch,'r',"latin_1")
        x=True
    except TypeError:
        sys.exit()

mch = re.search('(?=.*)([0-9]{9}_[0-9]{4}(_[0-9]+)(?=.*))',path,re.IGNORECASE)
src = mch.group()



#format src to correct structure for concatenence
psrc= u"þ"+src+u"þ\r\n"

#open and write attach.txt into OCRTEXT.DAT
n = codecs.open(path+'\\OCRTEXT.DAT','w',"latin_1")
frstln=u"þBegBatesþþEndBatesþþPgCountþþOCRþþSource Mediaþ\r\n"
n.write(frstln)
for line in f:
    n.write(line.replace("\r\n",psrc))
n.close()
f.close()

