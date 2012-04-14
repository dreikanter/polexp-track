import httplib
import urllib
import re
from sys import argv
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

if not re.match(r'^\d+$', argv[1]):
    print "Track ID not specified. Usage: track.py <track-id>"
    exit()

print "Requesting tracking info for consignment #%s..." % argv[1]

params = urllib.urlencode({'ctl00$ContentPlaceHolder1$txtAWB': argv[1],
		'tb_hid': 'on',
		'ctl00$ContentPlaceHolder1$txtUserId': 1395,
		'ctl00$ContentPlaceHolder1$txtPassword': 'ad8e6cf6',
		'ctl00$ContentPlaceHolder1$btn_TrackIt': 'submit',
		'__VIEWSTATE':'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',
		'__EVENTVALIDATION':'/wEWBgKSuK2VAgLJ7r3+DgL90KKTCALJ27D4DQLktKi0BQKekqTfCzcDfI4sOAABuhXYKhT2ULOq9/sJ'
	})

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

conn = httplib.HTTPConnection("polar.aimsdespatch.com")
conn.request("POST", "", params, headers)
response = conn.getresponse()
data = strip_tags(response.read())
tracks = re.findall(r'(\d\d-\d\d-\d\d \d\d:\d\d)([^\r\n]*)', data)
for item in tracks:
	print "%s: %s" % (item[0], item[1])
conn.close()