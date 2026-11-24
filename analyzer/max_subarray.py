"""Maximum-subarray algorithms for one buy/sell window.

Daily price changes are integers. The sum of a contiguous block equals the
profit of buying at the start of that block and selling at the end. When every
block loses money, the best choice is to skip the trade (profit 0).

The three routines return the same window: the greatest profit, then the
earliest buy, then the earliest sell.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Subarray:
    """Inclusive bounds into the change array. Empty means do not trade."""

    total: int
    start: int | None = None
    end: int | None = None

    @property
    def empty(self) -> bool:
        return self.start is None


EMPTY = Subarray(0)


def _prefer(left: Subarray, right: Subarray) -> Subarray:
    if left.total != right.total:
        return left if left.total > right.total else right
    if left.total <= 0:
        return EMPTY
    if left.start != right.start:
        return left if left.start < right.start else right
    if left.end != right.end:
        return left if left.end < right.end else right
    return left


def brute_force(values: list[int]) -> Subarray:
    """Check every pair of endpoints. Time O(n^2), extra space O(n)."""

    best = EMPTY
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    for start in range(len(values)):
        for end in range(start, len(values)):
            total = prefix[end + 1] - prefix[start]
            if total > 0:
                best = _prefer(best, Subarray(total, start, end))
    return best


ALGORITHMS: dict[str, Callable[[list[int]], Subarray]] = {
    "brute_force": brute_force,
}

COMPLEXITY = {
    "brute_force": "O(n^2)",
}
