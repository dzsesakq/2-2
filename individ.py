#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"b", "e", "f", "k", "t"}
    b = {"f", "i", "j", "p", "y"}
    c = {"j", "k", "l", "y"}
    d = {"i", "j", "s", "t", "u", "y", "z"}
    x = (a.union(c)).union((b.union(c)))
    print(f"x = {x}")
    # Найдем дополнения множеств
    bn = u.difference(b)
    y = (a.intersection(bn)).union(c.difference(d))
    print(f"y = {y}")
