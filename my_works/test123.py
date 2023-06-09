import inspect
import sys


def plus(a, b):
    return a + b


def test1():
    assert plus(2, 2) == 4


def test2():
    assert plus(100, 9) == 108


def test3():
    assert plus(-1, 1) == 0


def test4():
    assert plus(0, 0) == 0

