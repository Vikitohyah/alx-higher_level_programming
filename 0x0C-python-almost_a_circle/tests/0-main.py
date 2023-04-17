#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    B1 = Base()
    print(b1.id)

    B2 = Base()
    print(b2.id)

    B3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
