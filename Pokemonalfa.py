#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2

#url = 'https://bulbapedia.bulbagarden.net/wiki/Viridian_Forest'
url = "https://www.serebii.net/rb/greenblue.shtml"
data = urllib2.urlopen(url)
l = []
s = ''
for line in data.readlines():
    l.append(line)
s = '\n'.join(l)

print(l)