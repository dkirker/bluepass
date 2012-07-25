#!/usr/bin/env python
#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012
# Geert Jansen. All rights are reserved.
#
# This script generates AES test vectors of different lengths. The
# test vectors are created by encrypting random input via "openssl"
# command line utility to encrypt random input.

import os
import sys
import time
from subprocess import Popen, PIPE

sys.stdout.write('# Generated by: %s on %s\n' % (sys.argv[0], time.ctime()))

for keysize in (16, 24, 32):
    for ptlen in (0, 8, 14, 15, 16, 23, 31, 32, 42, 48, 64):
        key = os.urandom(keysize)
        iv = os.urandom(16)
        pt = os.urandom(ptlen)
        algo = '-aes-%d-cbc' % (keysize*8)
        cmd = Popen(['openssl', 'enc', '-e', algo, '-K', key.encode('hex'),
                    '-iv', iv.encode('hex')], stdin=PIPE, stdout=PIPE)
        ct, stderr = cmd.communicate(pt)
        sys.stdout.write('\n')
        sys.stdout.write('PT=%s\n' % pt.encode('hex'))
        sys.stdout.write('KEY=%s\n' % key.encode('hex'))
        sys.stdout.write('IV=%s\n' % iv.encode('hex'))
        sys.stdout.write('CT=%s\n' % ct.encode('hex'))