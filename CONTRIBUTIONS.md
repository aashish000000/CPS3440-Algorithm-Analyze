# Contributions

CPS 3440, Kean University. This file lists what each team member is responsible for and two resume bullets that describe their own work. The commits and pull requests in this repository show who pushed each part.

<!-- BEGIN:aashish -->
_Aashish: responsibilities and resume bullets (added when his part is finished)._
<!-- END:aashish -->

<!-- BEGIN:bhartendra -->
_Bhartendra: responsibilities and resume bullets (added when his part is finished)._
<!-- END:bhartendra -->

<!-- BEGIN:aron -->
## Aron Dardouri — Kadane's algorithm

Responsibilities: Kadane's one-pass maximum-subarray algorithm in `analyzer/max_subarray.py` and its tests.

Also owns (can explain and defend): the Top-K code in `analyzer/top_k.py` (merge sort, binary heap, quickselect) and `tests/test_top_k.py`, and the pseudocode and correctness notes in `docs/algorithms.md`. Top-K was originally planned for Brian Lucero, who left the project, so ownership moved to Aron.

Resume bullets:
- Implemented Kadane's Θ(n) time, Θ(1) space algorithm for the best single buy and sell on 26 years of S&P 500 data, and showed it agrees with the brute-force and divide-and-conquer answers on every tested input.
- Measured 311 ms at one million records with a log-log slope of 1.01 across 1,000 to 1,000,000 records, about four times faster than divide and conquer, and used the result to recommend Kadane as the algorithm to ship.
<!-- END:aron -->

## Shared work

The technical paper and the presentation are still being prepared and will be added to the repository.

## Notes

- Brute force at 100,000 and 1,000,000 records is an n¬≤ projection from the 10,000-record median, not a measurement.
- Timings vary by machine and by run, especially the million-record sort. Re-run the benchmark before quoting them.

<img width="462" height="417" alt="image" src="https://github.com/user-attachments/assets/1ec6dd3a-2177-4810-9674-19bca9155938" />
