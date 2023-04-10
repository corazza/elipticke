import math
from typing import Tuple

from common import *

KS = []
KS.append((1, 1, -1, -6, 0))
KS.append((0, 0, 7, 8, -16))
KS.append((1, 1, -1, 0, -8))
P1 = (-4, 0)
P2 = (-2.0/3, 0)


def main():
    for k in KS:
        report_curve(k)
        print()


if __name__ == '__main__':
    main()
