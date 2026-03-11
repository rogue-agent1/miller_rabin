#!/usr/bin/env python3
"""Miller-Rabin primality test — probabilistic prime testing."""
import sys, random
def miller_rabin(n, k=20):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0: r += 1; d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True
if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{n} is {'probably prime' if miller_rabin(n) else 'composite'}")
    else:
        tests = [2,3,17,561,1009,1000000007,2147483647,999999999989]
        for n in tests:
            print(f"  {n:>15d}: {'prime' if miller_rabin(n) else 'composite'}")
