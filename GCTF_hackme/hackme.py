#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

data =[0x5f,0xf2,0x5e,0x8b,0x4e,0xe,0xa3,0xaa,0xc7,0x93,0x81,0x3d,0x5f,0x74,0xa3,0x9,0x91,0x2b,0x49,0x28,0x93,0x67]
ans = ""
for i in xrange(22):
    v5= i
    v16= i
    v18= 0
    v15= data[i]
    v13= i + 1
    v17= 0
    while(v17 < v13):
        v17= v17 + 1
        v18= 0x6d01788d * v18 + 12345

    v4= v18 & 0xffff
    #  print str(v15 ^ (v18 & 0xff))
    #  print str(hex(v15 ^ (v18 & 0xff)))
    ans+= chr(v15 ^ (v18 & 0xff))

print ans