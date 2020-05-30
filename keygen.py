#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 04:52:33 2020

@author: berk
"""

import string
import random

secenekler = string.digits + string.ascii_uppercase;

def kontrol(key):
    while 1:
        a=0;
        for char in key:
            a+=ord(char)
            a=a>>1
            a=a%3840
            a+=10
        soneleman=chr(a)
        if soneleman in secenekler:
            key += soneleman
            print(key)
            return

def key():
    i=0
    key=""
    while(i<15):
        key+=random.choice(secenekler)
        i+=1
    return key

kontrol(key())

    
