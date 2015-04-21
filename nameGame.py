#!/usr/bin/env python
import re, os, subprocess
while True:
  name = raw_input("Whats your name?")
  rgx = re.sub(r'^[^aeiouAEIOU]+([aeiouAEIOU].*)', r'\1', name)
  out = "%s %s bo-b%s, Bonana-Fanna Fo-F%s Fee-Fy mo-m%s, %s!" % (name,name,rgx,rgx,rgx,name)
  if os.uname()[0] == 'Darwin':
      subprocess.call(['/usr/bin/say', out])
  else:
      print out
