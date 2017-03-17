#!/usr/bin/env python
# encoding: utf-8
def str64(string):
    string = string.strip('0x')
    string = '0' * (16-len(string)) + string
    result = ['00'] * 8
    for i in range(0, 8):
        result[7 - i] = string[i*2: (i+1)*2]
    return ''.join('\\x' + i for i in result)


def str32(string):
    string = string.strip('0x')
    string = '0' * (8-len(string)) + string
    result = ['00'] * 4
    for i in range(0, 4):
        result[3 - i] = string[i*2: (i+1)*2]
    return ''.join('\\x' + i for i in result)


def strhex(string, bits):
    string = string.strip('0x')
    string = '0' * (bits/4 - len(string)) + string
    result = ['00'] * (bits / 8)
    for i in range(0, bits / 8):
        result[bits/8 - 1 - i] = string[i*2: (i+1)*2]
    return ''.join('\\x' + i for i in result)
