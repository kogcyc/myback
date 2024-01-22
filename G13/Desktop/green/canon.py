import sys
import requests
#
def getraw(modl):
	a = requests.get(f'https://en.wikipedia.org/wiki/Canon_EOS_{modl}')
	b = str(a.content)
#
	c = b.find('f{modl}')
	return b[c-100:c+200] + '\n'
#
modl = sys.argv[1]
d = getraw(modl)
print(d)