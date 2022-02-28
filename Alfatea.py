import urllib2

#url = 'https://bulbapedia.bulbagarden.net/wiki/Viridian_Forest'
url = 'http://gjerrestad.no/Tor/Kalkulatorer/Dusj/dusjkalk.htm'
data = urllib2.urlopen(url)
l = []
s = ''
for line in data.readlines():
    l.append(line)
s = '\n'.join(l)

print(l)