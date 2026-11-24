# Contributions

CPS 3440, Kean University. This file lists what each team member is responsible for and two resume bullets that describe their own work. The commits and pull requests in this repository show who pushed each part.

<!-- BEGIN:aashish -->
## Aashish Joshi — brute force (baseline)

Responsibilities: the brute-force maximum-subarray algorithm in `analyzer/max_subarray.py` and its tests.

Also owns (can explain and defend): the data loading and command-line tool (`analyzer/prices.py`, `analyzer/__main__.py`, `analyzer/report.py`, `analyzer/fetch.py` and `tests/test_prices.py`), the README and repository layout, and the Colab notebook.

Resume bullets:
- Implemented a Θ(n²) brute-force baseline for the best-buy/best-sell problem in Python and benchmarked it against Θ(n log n) and Θ(n) algorithms on 2.7 million rows of S&P 500 data.
- Measured 12.7 s at 10,000 records against 2.9 ms for a linear scan (about 4,400 times slower), fitted a log-log slope of 2.50 against the model value of 2, and projected 21 minutes at 100,000 and 35 hours at 1,000,000 records, labelled as projections and not measurements.
<!-- END:aashish -->

<!-- BEGIN:bhartendra -->
## Bhartendra Kumar Mandal — divide and conquer

Responsibilities: the divide-and-conquer maximum-subarray algorithm in `analyzer/max_subarray.py` (the crossing scan and the earliest-window tie rule) and its tests.

Also owns (can explain and defend): the benchmark runner and figures (`analyzer/benchmark.py`, `tests/test_benchmark.py`, `benchmarks/results.json`), and the site generator `docs/render.py` that builds the GitHub Pages site.

Resume bullets:
- Implemented the CLRS divide-and-conquer maximum-subarray algorithm, solved its recurrence T(n) = 2T(n/2) + Θ(n) with the Master Theorem, and checked it against the brute-force and Kadane implementations on the CLRS example and on real data.
- Verified the Θ(n log n) bound with an exact operation count (20,951,424 element reads at one million records) and measured 1.28 s at that size with a wall-clock slope of 1.04.
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
