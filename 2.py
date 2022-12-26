# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = set(input("Введите первую строку: "))
    b = set(input("Введите вторую строку: "))

    bn = u.difference(b)
    c = a.difference(bn)
    print(len(c), " - Кол-во общих элементов")
    print(c, " - Общие элементы")
