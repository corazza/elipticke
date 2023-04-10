import IPython
import math
from typing import Tuple

from common import *

KS = []
KS.append((625, 46875))
KS.append((1, 3))
KS.append((-3915, 113670))


"""
e = [0, 0, 0, -3915, 113670]
E = ellinit(e)
p = 17
p + 1 - ellap(E, p)
elltors(E)
gen=[-21, 432]
n = 0
ellpow(E, gen, n)
"""


def main():
    for k in KS:
        report_short_curve(k)
        d = short_discriminant(k)


if __name__ == '__main__':
    main()
