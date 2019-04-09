#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):


    n=len(a)
    i = 0

    while i < n - 1:
        smallest = i
        j = i + 1

        while j < n:
            if a[j] < a[smallest]:
                smallest = j  #нахдим наименьшее число
            j += 1

        a[i], a[smallest] = a[smallest], a[i]  # меняем местами, наименьшее "вначало"

        # print(a)

        i += 1

    return a