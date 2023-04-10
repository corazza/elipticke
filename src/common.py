from sympy import factorint
import math
from typing import Tuple

# y^2 + a1xy + a3y = x^3 + a2x^2 + a4x + a6
CURVE = Tuple[int, int, int, int, int]
SHORT_CURVE = Tuple[int, int]
B_PARAM = Tuple[int, int, int, int]
C_PARAM = Tuple[int, int]


def short_curve(a: int, b: int) -> CURVE:
    return 0, 0, 0, a, b


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
    return f'y^2 = x^3 + ({a})x + ({b})'


def discriminant(k: CURVE) -> int:
    c4, c6 = c_param(k)
    return int((c4**3 - c6**2)/1728)


def short_discriminant(k: SHORT_CURVE) -> int:
    a, b = k
    return -16*(4*a**3 + 27*b**2)


def j_invariant(k: CURVE) -> int:
    c4, c6 = c_param(k)
    d = discriminant(k)
    return (c4**3 / d)


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


def pretty_discriminant(d: int) -> str:
    factors = factorint(d)
    result = '-' if -1 in factors else ''
    for factor, power in factors.items():
        if factor == -1:
            continue
        result = result + f'{factor}^{power} '
    return result


def report_short_curve(k: SHORT_CURVE):
    a, b = k
    print(f'a={a}, b={b}')
    d = short_discriminant(k)
    print(f'discriminant = {d} = {pretty_discriminant(d)}')
    print(f'delta_0 = {d//16} = {pretty_discriminant(d//16)}')


def polynomial(k: CURVE, p: Tuple[float, float]) -> float:
    a1, a3, a2, a4, a6 = k
    x, y = p
    return x**3 + a2*x**2 + a4*x + a6 - y**2 - a1*x*y - a3*y


def test_point(k: CURVE, p: Tuple[float, float]) -> bool:
    return polynomial(k, p) == 0
