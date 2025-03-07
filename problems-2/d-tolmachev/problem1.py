#!/usr/bin/env python3

import math
from typing import Iterable

# Generates Pythagorean triples with elements less than the specified number
def pythagorean_triples(l: int) -> Iterable[tuple[int]]:
    return ((pow(m, 2) - pow(n, 2), 2 * m * n, pow(m, 2) + pow(n, 2)) for m in range(2, math.ceil(math.sqrt(l))) for n in range(1, min(math.floor(math.sqrt(l - pow(m, 2))) + 1, m)))    # O(k) where k -- number of generated triplets

# Used as entrypoint
if __name__ == '__main__':
    print(tuple(pythagorean_triples(16)))
