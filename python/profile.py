'''
Created on Feb 11, 2013

@author: jtesta
'''

import os
from datetime import datetime


_proc_status = '/proc/%d/status' % os.getpid()

_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

clock_start = datetime.now()
clock_end = datetime.now()


def start_clock():
    global clock_start
    clock_start = datetime.now()

#Should only be called once the clock has been started. Otherwise 
#counts the time from when the module was imported.
def get_time_from_clock():
    global clock_start, clock_end
    clock_end = datetime.now()
    difftime = clock_end - clock_start
    clock_start = clock_end
    return difftime

def filesize(filename):
    return os.stat(filename).st_size

def vmB(VmKey):
    global _proc_status, _scale
     # get pseudo file  /proc/<pid>/status
    try:
        t = open(_proc_status)
        v = t.read()
        t.close()
    except:
        return 0.0  # non-Linux?
     # get VmKey line e.g. 'VmRSS:  9999  kB\n ...'
    i = v.index(VmKey)
    v = v[i:].split(None, 3)  # whitespace
    if len(v) < 3:
        return 0.0  # invalid format?
     # convert Vm value to bytes
    return float(v[1]) * _scale[v[2]]


def memory(since=0.0):
    '''Return memory usage in bytes.
    '''
    return vmB('VmSize:') - since


def resident(since=0.0):
    '''Return resident memory usage in bytes.
    '''
    return vmB('VmRSS:') - since


def stacksize(since=0.0):
    '''Return stack size in bytes.
    '''
    return vmB('VmStk:') - since

    
    
if __name__ == '__main__':
    pass
