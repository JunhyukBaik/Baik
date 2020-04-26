#!/usr/bin/python3

def union(a, b):
    print("=>union ", end='')
    print(list(set(a).union(b)))

def intersection(a, b):
    print("=>intersection ", end='')
    print(list(set(a).intersection(b)))
