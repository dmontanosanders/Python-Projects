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




url = 'http://192.168.1.74/hp/device/this.LCDispatcher?nav=hp.Usage' # write the url here

usock = urllib2.urlopen(url)
data = usock.read()
msend = re.search(r'(?=Send Job Scan Count<\/span>\n).*',data)
usock.close()

print msend.group()

