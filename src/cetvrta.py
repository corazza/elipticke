import IPython
import numpy as np


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
        print(
            f'i={i}, n_{i}={b[i]}, c_{i}={c[i]}, n_{i+1}={b[i+1]} --> c_{i+1}={c[i+1]}, s_{i}={s[i]}')
    return s


def prvi():
    n: int = 96
    nas: np.ndarray = nas_rep(n)
    print(nas)


def main():
    prvi()


if __name__ == '__main__':
    main()
