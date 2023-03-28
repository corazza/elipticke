import math
from typing import Tuple

CURVE = Tuple[int, int, int, int, int]
B_PARAM = Tuple[int, int, int, int]
C_PARAM = Tuple[int, int]

KS = []
KS.append((1, 1, -1, -6, 0))
KS.append((0, 0, 7, 8, -16))
KS.append((1, 1, -1, 0, -8))
P1 = (-4, 0)
P2 = (-2.0/3, 0)


def b_param(k: CURVE) -> B_PARAM:
    a1, a3, a2, a4, a6 = k
    b2 = a1**2 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3**2 + 4*a6
    b8 = int(1.0/4 * (b2*b6 - b4**2))
    return b2, b4, b6, b8


def _c_param(b: B_PARAM) -> C_PARAM:
    b2, b4, b6, b8 = b
    c4 = b2**2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    return c4, c6


def c_param(k: CURVE) -> C_PARAM:
    b = b_param(k)
    return _c_param(b)


def short_weierstrass(k: CURVE) -> Tuple[int, int]:
    c4, c6 = c_param(k)
    return -27*c4, -54*c6


def pretty_short_weierstrasss(k: CURVE) -> str:
    a, b = short_weierstrass(k)
    return f'y^2 = x^2 + ({a})x + ({b})'


def discriminant(k: CURVE) -> int:
    c4, c6 = c_param(k)
    return int((c4**3 - c6**2)/1728)


def j_invariant(k: CURVE) -> int:
    c2, c4 = c_param(k)
    d = discriminant(k)
    return int(c4**3 / d)


def report_curve(k: CURVE):
    b = b_param(k)
    c = _c_param(b)
    print(f'a1={k[0]} a3={k[1]} a2={k[2]} a4={k[3]} a6={k[4]}')
    print(f'b2={b[0]} b4={b[1]} b6={b[2]} b8={b[3]}')
    print(f'c2={c[0]} c4={c[1]}')
    print(f'short weierstrass: {pretty_short_weierstrasss(k)}')
    d = discriminant(k)
    print(f'discriminant={d}')
    if d != 0:
        print(f'j-invariant={j_invariant(k)}')


def polynomial(k: CURVE, p: Tuple[float, float]) -> float:
    a1, a3, a2, a4, a6 = k
    x, y = p
    return x**3 + a2*x**2 + a4*x + a6 - y**2 - a1*x*y - a3*y


def test_point(k: CURVE, p: Tuple[float, float]) -> bool:
    return polynomial(k, p) == 0


def main():
    for k in KS:
        report_curve(k)
        print()


if __name__ == '__main__':
    main()
