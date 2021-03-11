import os

base = os.path.abspath(os.path.dirname(__file__))

def test(a):
    zw=a*12
    print(base)

def baa():
    return base

def main():
    a = input()
    test(a)
    print(base)

main()
