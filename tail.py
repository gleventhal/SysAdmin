#!/usr/bin/python
import sys, os
MAX_LINES = 10

def usage():
  sys.stderr.write("Usage: %s FILE\n" % sys.argv[0])

if len(sys.argv) > 1:
  args = sys.argv[1:]
  if len(args) > 1:
    try:
      if args[0] == '-n':
        MAX_LINES = args[1]
        FILE = args[2]
      else:
        FILE = args[0]
        if args[1] == '-n':
          MAX_LINES = args[2]
        else:
          usage()
    except:
      usage()
  else:
    FILE = args[0]
else:
  usage()

if os.path.isfile(FILE):
  with open(FILE, 'r') as f:
    buf = ''
    nl_count = 0
    f.seek(0, os.SEEK_END)
    while f.tell() > 0 and nl_count < MAX_LINES:
      char = f.read(1)
      if char == '\n': nl_count += 1
      if nl_count < int(MAX_LINES):
        buf = char + buf
        f.seek(-2,1)
      else:
        break
  print(buf)
else:
  usage()
