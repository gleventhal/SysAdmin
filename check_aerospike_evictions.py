#!/usr/bin/env python
#
import subprocess
import sys, os

# Globals
output_dict = {}
input_dict = {}
eviction_threshold = '0'
output = subprocess.Popen(['/usr/bin/asmonitor', '-e info'], stdout=subprocess.PIPE).communicate()[0]
output = output[output.index('ip/namespace'):len(output)]
errors = []

def Usage():
    print "Usage %s: \"'namespace1' : <max eviction number>, 'namespace2' : 400\"" % os.path.basename(__file__)
    print "i.e: %s \"user_profiles_3d:5000\"" % os.path.basename(__file__)
    sys.exit(1)

def mainLoop():
    ''' Check user-specified eviction thresholds against specified namespaces '''
    for line in output.split('\n')[3:len(output.split('\n')) - 2]:
        line = filter(None, line.split(' '))
        output_dict[line[0]] = line[2].replace(',','')
        ##############################
    for namespace, evictions in output_dict.items():
        if namespace.split('/')[1] in input_dict.keys():
            if int(evictions) > int(input_dict[namespace.split('/')[1]]):
                errors.append("%s has %s evictions, exceeding the threshold by %d" % \
                (namespace.replace(',','').split('/')[1], evictions.replace(',',''), int(evictions.replace(',','')) - int(input_dict[namespace.split('/')[1]])))

if len(sys.argv) < 2:
    Usage()
else:
    input_dict[sys.argv[1].split(':')[0]] = sys.argv[1].split(':')[1]
    mainLoop()

if errors:
    print "\n".join(errors)
    sys.exit(1)
else:
    print "OK:"
    sys.exit(0)
~                                                                                                                                                                                                                               
~                        
