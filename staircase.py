# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:40:55 2020

@author: rohith
"""


def staircase(n):
        for i in range(n):
            for j in range (n):
                if i+j == n-1:
                    print(" "*j+"#"*(n-j))


if __name__ == '__main__':
    n = int(input())

    staircase(n)

