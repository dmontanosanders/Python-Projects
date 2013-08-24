#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel
#
# Created:     13/06/2013
# Copyright:   (c) Daniel 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2,re
from bs4 import BeautifulSoup
from xlrd import open_workbook,XL_CELL_TEXT
from xlwt import Workbook
from xlutils.copy import copy

def get_mreads(x):

    url = 'http://'+x+'/hp/device/this.LCDispatcher?nav=hp.Usage' # write the url here

    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()

    soup = BeautifulSoup(data)
    srlnumht = soup.find(id="Text2")
    srlnum = srlnumht.get_text()
    return srlnum

rb = open_workbook('Book1.xlsx')
sheet = rb.sheet_by_name('IP Address')

cell = sheet.cell(1,1)
if cell.value == "yes":
    ipaddr = sheet.cell(1,0)
    test = get_mreads(ipaddr.value)

wb = copy(rb)
wb.get_sheet(1).write(1,0,test)
wb.save('Book2.xls')



