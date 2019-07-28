#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# file from https://github.com/Nircek/languages-drop
# licensed under MIT license

'''
MIT License

Copyright (c) 2019 Nircek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


def getter(_in):
    out = ''
    while True:
        n = _in()
        if not n:
            break
        out += n + '\n'
    return out


def analyze(string):
    p = {}
    for e in string.split('\n')[:-1]:
        e = e.split(' ')
        if e[0] not in p:
            p[e[0]] = []
        p[e[0]] += e[1:]
    return p


def process(data):
    p = {}
    for e in data.keys():
        if e not in p.keys():
            p[e] = []
        for f in data[e]:
            f = f.split('\'')
            if '-' in f[0]:
                year = f[1]
                f = f[0].split('-')
                for i in range(int(f[0]), int(f[1])+1):
                    j = ('0' + str(i))[-2:]
                    p[e] += [(j, year)]
            else:
                year = f[1]
                month = f[0]
                p[e] += [(month, year)]
    return p


_in = getter(input)
x = process(analyze(_in))
a = []
for e in x.keys():
    a += x[e]
a = [(y, x) for x, y in a]
a.sort()
a = [(int(y), int(x)) for x, y in a]
min = a[1]
max = a[-1]
x = {'date': [], **x}
for e in x:
    print(e, end=' ')
    for year in range(min[1], max[1]+1):
        for month in range(1, 13):
            if year == min[1] and month < min[0]:
                continue
            if year == max[1] and month > max[0]:
                continue
            string = ('0' + str(month))[-2:]+'\''+str(year)
            if e == 'date':
                print(string, end=' ')
            else:
                print(1 if (tuple(string.split('\'')) in x[e]) else 0, end=' ')
    print()
