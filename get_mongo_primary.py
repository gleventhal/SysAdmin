#!/usr/bin/env python
import re, urllib

mongo_web_interface = 'http://Server:Port/_replSet'
r = urllib.urlopen(mongo_web_interface)
ui = map(lambda x: re.findall('(e-[^:]*):', x), [ui for ui in r.readlines() if 'PRIMARY' in ui])
print set(max(ui)).pop()
