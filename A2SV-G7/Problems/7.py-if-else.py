#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (not n%2 and n in range(6, 21)) or n % 2:
        print("Weird")
    elif (not n%2 and n in range(2, 6)) or (not n%2 and n > 20):
        print("Not Weird")