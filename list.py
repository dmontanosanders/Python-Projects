#! C:\Python27
# -*- coding: latin_1 -*-
import easygui as eg
import os
import re


path = eg.diropenbox("","Choose Folder with .CSV files","C:\\")
n = open(path+"\\RFPs.txt",'w')
#get all files in dir
for root, dirs, files in os.walk(path):
    for filename in files:
#test if file is .csv and proceed if true
        if filename.endswith(".csv"):
            #get number of lines in .csv
            nl = len(open(path+"\\"+filename).readlines())
            #write filename in file and add newline
            n.write(filename+":\n")
            #open the file for reading line by line
            f=open(path+"\\"+filename,'r')
            #set line count to zero for every file
            x=0
            for line in f:
                #strip newline and split each line at comma. test if begdoc
                #matches enddoc for single page docs and eof
                linen = line.rstrip('\n')
                ls = linen.split(',')
                if ls[0]==ls[1]:
                    if x==nl-1:
                        n.write(ls[0]+"\n\n")
                    else:
                        n.write(ls[0]+", ")
                        x=x+1
                #check if eof and write last line with newline
                elif x==nl-1:
                    line = line.rstrip('\n')
                    n.write(line.replace(',','-')+"\n\n")
                #write line if not single page and proceed to next line
                else:
                    line = line.replace(',','-')
                    n.write(line.replace('\n',', '))
                    x=x+1
            f.close()

n.close






