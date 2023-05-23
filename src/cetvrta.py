import IPython
import numpy as np
import pyperclip


def bin_rep(n: int) -> list[int]:
    result: list[int] = []
    while n > 0:
        result.append(n % 2)
        n //= 2
    return result[::-1]


def nas_rep(n: int) -> np.ndarray:
    b: np.ndarray = np.array(
        list(reversed([0, 0] + bin_rep(n))), dtype=np.int8)
    s: np.ndarray = np.zeros(len(b)-1, dtype=np.int8)
    c: np.ndarray = np.zeros(len(b), dtype=np.int8)
    for i in range(len(b)-1):
        c[i+1] = int(np.floor((b[i] + b[i+1] + c[i])/2))
        s[i] = b[i] + c[i] - 2*c[i+1]
        # print(
        #     f'i={i}, n_{i}={b[i]}, c_{i}={c[i]}, n_{i+1}={b[i+1]} --> c_{i+1}={c[i+1]}, s_{i}={s[i]}')
    return s


# def binary_ladder(m: np.ndarray, P: tuple[int, int]) -> tuple[int, int]:
#     d: int = len(m)
#     Q: tuple[int, int] = P
#     Q = 53, 77
#     for i in range(d - 2, -1, -1):
#         Q = (2*Q[0], 2*Q[1])
#         print(f'i={i}, Q={}')
#         if m[i] == 1:
#             Q = (Q[0] + P[0], Q[1] + P[1])
#         if m[i] == -1:
#             Q = (Q[0] - P[0], Q[1] - P[1])
#     return Q


def prvi():
    n: int = 96
    P: tuple[int, int] = (0, 2)
    nas: np.ndarray = nas_rep(n)
    print(nas)  # [0  0  0  0  0 -1  0  1]
    # q = binary_ladder(nas, P)
    # print(q)

    # E = ellinit([2, 4])
    # Et = ellinit(E, 211)
    # ellmul(Et, [0, 2], 96)

    # [Mod(56, 211), Mod(32, 211)]

    # => 96P = (56, 32)


def drugi():
    rows = [f'iferr(ellap(ellinit([0,0,0,{i},{j}], 17)), print("Bad curve parameters"));'
            for j in range(1, 20) for i in range(1, 20)]
    x: str = '\n' + '\n'.join(rows)
    pyperclip.copy(x)


def main():
    prvi()
    # ellap(ellinit([0,0,0,3,2], 17))
    drugi()

    # ellinit([0, 0, 0, 6, 17])

    # treci

    # [0]
    # [Mod(3, 191), Mod(15, 191)]
    # [Mod(11, 191), Mod(3, 191)]
    # [Mod(36, 191), Mod(130, 191)]
    # [Mod(178, 191), Mod(116, 191)]
    # [Mod(164, 191), Mod(106, 191)]
    # [Mod(120, 191), Mod(168, 191)]
    # [Mod(133, 191), Mod(6, 191)]

    # [Mod(143, 191), Mod(12, 191)]
    # [Mod(36, 191), Mod(130, 191)]
    # [Mod(164, 191), Mod(85, 191)]
    # [Mod(30, 191), Mod(26, 191)]
    # [Mod(92, 191), Mod(162, 191)]
    # [Mod(83, 191), Mod(163, 191)]
    # [Mod(67, 191), Mod(188, 191)]
    # [Mod(87, 191), Mod(44, 191)]

    # P=[3,15]
    # E=ellinit([0,0,0,1,4], 191)

    # print("computing Q:")
    # Q = ellmul(E, P, 191+1+27)
    # print(Q)

    # print("computing [j]P:")
    # P0 = ellmul(E, P, 0)
    # P1 = ellmul(E, P, 1)
    # P2 = ellmul(E, P, 2)
    # P3 = ellmul(E, P, 3)
    # P4 = ellmul(E, P, 4)
    # P5 = ellmul(E, P, 5)
    # P6 = ellmul(E, P, 6)
    # P7 = ellmul(E, P, 7)
    # print(P0)
    # print(P1)
    # print(P2)
    # print(P3)
    # print(P4)
    # print(P5)
    # print(P6)
    # print(P7)
    # print("done")

    # print("computing R = [8]P:")
    # R = ellmul(E, P, 8)
    # print(R)

    # print("computing R[i]")
    # R0 = ellmul(E, R, 0)
    # R1 = ellmul(E, R, 1)
    # R2 = ellmul(E, R, 2)
    # R3 = ellmul(E, R, 3)
    # R4 = ellmul(E, R, 4)
    # R5 = ellmul(E, R, 5)
    # R6 = ellmul(E, R, 6)
    # R7 = ellmul(E, R, 7)
    # print(R0)
    # print(R1)
    # print(R2)
    # print(R3)
    # print(R4)
    # print(R5)
    # print(R6)
    # print(R7)
    # print("done")

    # print("computing diff:")
    # print(ellsub(E, Q, R0))
    # print(ellsub(E, Q, R1))
    # print(ellsub(E, Q, R2))
    # print(ellsub(E, Q, R3))
    # print(ellsub(E, Q, R4))
    # print(ellsub(E, Q, R5))
    # print(ellsub(E, Q, R6))
    # print(ellsub(E, Q, R7))


if __name__ == '__main__':
    main()
