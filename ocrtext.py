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
    path = eg.diropenbox("","Choose EXPORT Folder","K:\\"+my)
    try:
        f = codecs.open(path+'\\attach.txt','r',"latin_1")
        x=True
    except TypeError:
        sys.exit()
    except :
        if eg.ynbox("There is no 'attach.txt' file in the folder you selected\nWould you like to Continue?","Whoops, that didn't work!"): pass
        else:
            sys.exit()
#resolve source from path
mch = re.search('[0-9]{9}_[0-9]{4}.*(?=\.SCL)',path,re.IGNORECASE)
src = mch.group()

#format src to correct structure for concatenence
psrc= u"þ"+src+u"þ\r\n"

#open and write attach.txt into OCRTEXT.DAT
n = codecs.open(path+'\\OCRTEXT.DAT','w',"latin_1")
frstln=u"þBegBatesþþEndBatesþþPgCountþþOCRþþSource Mediaþ\r\n"
n.write(frstln)
for line in f:
    n.write(line.replace("\r\n",psrc))
n.close()
f.close()

#delete txt files in source directory
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".txt"):
            os.remove(os.path.join(root,filename))



