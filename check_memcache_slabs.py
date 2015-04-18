#!/usr/bin/env python
import subprocess
import re, sys
WARNING = []
myDict = {}

# If a file is passed as ARG 1, treat it as stats slabs data to parse, otherwise request data from Memcached directly
if not len(sys.argv) > 1:
    file = '/tmp/memcache_slabs.tmp'
    with open(file, 'w') as m:
        stats = subprocess.Popen(('echo', 'stats slabs'), stdout=subprocess.PIPE)
        output = subprocess.check_call(('nc', '-w 10', 'localhost', '11228'), stdin=stats.stdout, stdout=m)
else:
    file = sys.argv[1]

# Analyze slabs stats, splitting into a dictionary of type: { slab class : [ stats ] }
with open(file, 'r') as f:
    for line in f.readlines():
        l = line.split(':')
        if l[0] in myDict.keys():
            myDict[l[0]].append(l[1].strip())
        else:
            myDict[l[0]] = []
        try:
            myDict[l[0]].append(l[1])
        except IndexError:
            pass

for k in myDict.keys():
    free_chk_end = [result for result in map(lambda i: re.findall('free_chunks_end (\d+)', str(i)), myDict[k]) if len(result) > 0]
    try:
        if free_chk_end[0][0] == 0:
            WARNING.append("%s slab is FULL" % (k))
        elif 'outofmemory' in myDict[k]:
            WARNING.append("%s slab is OOM" % (k))
        else:
            pass
    except IndexError:
        pass

if WARNING:
    print 'WARNING: ' + (('\t').join(WARNING))
    sys.exit(1)
else:
    print "OK"

