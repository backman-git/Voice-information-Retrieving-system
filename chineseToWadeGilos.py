import urllib2, urllib

data = {'cw' :"dd"}
f = urllib2.urlopen(
        url     = 'http://billor.chsh.chc.edu.tw/php/Tools/qPining.php',
        data    = urllib.urlencode(data)
		)
print f.read()