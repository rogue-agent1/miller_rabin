#!/usr/bin/env python3
"""Miller-Rabin primality test — probabilistic prime testing.

One file. Zero deps. Does one thing well.

Deterministic for n < 3,317,044,064,679,887,385,961,981 using specific witness sets.
"""
import sys, random

def miller_rabin(n, k=20):
    """Test if n is probably prime with k rounds."""
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    # Write n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Deterministic witnesses for small n
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 3215031751:
        witnesses = [2, 3, 5, 7]
    elif n < 3317044064679887385961981:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    else:
        witnesses = [random.randrange(2, n - 1) for _ in range(k)]

    for a in witnesses:
        if a >= n: continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def next_prime(n):
    if n < 2: return 2
    n = n + 1 if n % 2 == 0 else n + 2
    while not miller_rabin(n):
        n += 2
    return n

def prime_range(lo, hi):
    """All primes in [lo, hi]."""
    return [n for n in range(max(2, lo), hi + 1) if miller_rabin(n)]

def main():
    # Test known primes/composites
    primes = [2, 3, 5, 7, 11, 13, 97, 997, 7919, 104729, 15485863, 2147483647]
    composites = [4, 6, 8, 9, 15, 100, 561, 1105, 1729]  # 561,1105,1729 = Carmichael numbers
    print("Primes:")
    for p in primes:
        assert miller_rabin(p), f"{p} should be prime"
        print(f"  {p:>12d} ✓")
    print("Composites (including Carmichael numbers):")
    for c in composites:
        assert not miller_rabin(c), f"{c} should be composite"
        print(f"  {c:>12d} ✗")
    # Big primes
    big = 2**61 - 1  # Mersenne prime
    print(f"\n2^61 - 1 = {big}: prime={miller_rabin(big)}")
    big2 = 2**89 - 1  # Mersenne prime
    print(f"2^89 - 1: prime={miller_rabin(big2)}")
    # Next prime
    print(f"\nnext_prime(100) = {next_prime(100)}")
    print(f"next_prime(10**9) = {next_prime(10**9)}")

if __name__ == "__main__":
    main()
