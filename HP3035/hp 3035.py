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

import urllib2,re,datetime
from bs4 import BeautifulSoup
from xlrd import open_workbook,XL_CELL_TEXT
from xlwt import Workbook
from xlutils.copy import copy

def get_newmreads(x): # Get meter reads for firmware version 48.283.4

    url = 'http://'+x+'/hp/device/this.LCDispatcher?nav=hp.Usage' # write the url here
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    soup = BeautifulSoup(data)
    srlnum = soup.find(id="Text2").get_text()
    srlloc = soup.find(id="Text4").get_text()
    copynum = soup.find(id="Text171").get_text()
    sendnum = soup.find(id="Text251").get_text()
    totalnum = soup.find(id="Text277").get_text()
    printnum = int(totalnum) - int(copynum)
    return srlnum

def get_oldmreads(x): # Get meter reads for firmware version 48.131.3

    url = 'http://'+x+'/hp/device/this.LCDispatcher?nav=hp.Usage' # write the url here
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    soup = BeautifulSoup(data)
    srlnum = soup.find(id="Text2").get_text()
    return srlnum

def chk_firm(x): # check printer firmware version

    url = 'http://'+x+'/hp/device/this.LCDispatcher?nav=hp.Config'
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    soup = BeautifulSoup(data)
    firm = soup.find(id="Text18").get_text()
    return firm

#d = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
rb = open_workbook('MeterReads.xls')
sheet = rb.sheet_by_name('IP Address')
n = 1
while n < 33:
    cell = sheet.cell(n,1)
    if cell.value == "Yes":
        ipaddr = sheet.cell(n,0)
        test = chk_firm(ipaddr.value)
        n += 1
#wb = copy(rb)
#wb.get_sheet(1).write(1,0,test)
#wb.save('Book2.xls')


