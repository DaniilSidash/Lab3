#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составьте программу, которая печатает таблицу умножения натуральных чисел в
# десятичной системе счисления

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, 10):
            print("%4d" % (i * j), end='')
        print()
