#!/usr/bin/python
import sys, os, time, re
NUM_LINES = int(sys.argv[2])

def tail_f(FILE):
  if not os.path.isfile(FILE):
    raise(Exception("E_Not_File: %s" % FILE))
  with open(FILE, 'r') as f:
    f.seek(0, os.SEEK_END)
    ncount = 0
    while f.tell() != 0 and ncount < NUM_LINES:
      f.seek(-2, 1)
      last_char = f.read(1)
      if last_char == '\n':
        ncount += 1
    for line in f:
      sys.stdout.write(line)
    while 1:
      last = f.readline()
      if not last:
        time.sleep(0.1)
      sys.stdout.write(last)

tail_f(sys.argv[1])
