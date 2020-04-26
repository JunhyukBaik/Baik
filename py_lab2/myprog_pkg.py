#!/usr/bin/python3
import my_pkg
import re

if __name__ == '__main__':
    while(True):
        num = int(input("Select menu: 1)conversion  2)union/intersection 3)exit? "))
        if(num==1):
            data = int(input("input binary number : "), 2)
            my_pkg.print_oct(data)
            my_pkg.print_dec(data)
            my_pkg.print_hex(data)
        if(num==2):
            a = input("1st list: ")
            a = re.sub("\[","",a)
            a = re.sub("\]","",a)
            list1 = list(map(int,re.split(r"[,\s]+", a)))
            b = input("2nd list: ")
            b = re.sub("\[","",b)
            b = re.sub("\]","",b)
            list2 = list(map(int, re.split(r"[,\s]+", b)))
            my_pkg.union(list1, list2)
            my_pkg.intersection(list1, list2)
        if(num==3):
            print('exit the program...')
            break
