# -*- coding:utf-8 -*-
import itertools

__author__ = 'ngnono'

# string processing

def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)


def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)


def isNoneOrEmpty(s):
    if s is None:
        return True

    if len(s.strip()) == 0:
        return True

    return False

