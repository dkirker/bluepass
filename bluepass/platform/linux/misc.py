#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012-2013
# Geert Jansen.
#
# Bluepass is free software available under the GNU General Public License,
# version 3. See the file LICENSE distributed with this file for the exact
# licensing terms.

import os

def get_machine_info():
    """Return a tuple (hostname, os, arch, cores, cpu_speed, memory)."""
    osname, hostname, dummy, dummy, arch = os.uname()
    cores = 0
    fin = file('/proc/cpuinfo')
    for line in fin:
        line = line.strip()
        if not line:
            continue
        label, value = line.split(':')
        label = label.strip(); value = value.strip()
        if label == 'processor':
            cores += 1
    fin.close()
    try:
        fin = file('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq')
        cpu_speed = int(fin.readline().strip()) / 1000
        fin.close()
    except IOError:
        cpu_speed = 0
    memory = 0
    fin = file('/proc/meminfo')
    for line in fin:
        line = line.strip()
        if not line:
            continue
        label, value = line.split(':')
        label = label.strip(); value = value.strip()
        if label == 'MemTotal':
            value = value.rstrip('kB')
            memory = int(value) / 1000
            break
    return (hostname, osname, arch, cores, cpu_speed, memory)
