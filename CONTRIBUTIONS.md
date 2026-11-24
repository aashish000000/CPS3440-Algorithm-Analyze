# Contributions

CPS 3440, Kean University. This file lists what each team member is responsible for, how their algorithm works, the results they measured, and two resume bullets that describe their own work. The commits and pull requests in this repository show who pushed each part.

All timings were measured on one laptop with five trials and the median reported. They vary by machine. The data is the Kaggle S&P 500 file (2,703,531 rows, 472 tickers, 2000-01-03 to 2026-02-20).

## Aashish Joshi: brute-force baseline, data loading, command-line tool

**Files:** `analyzer/max_subarray.py` (the `brute_force` function), `analyzer/prices.py`, `analyzer/report.py`, `analyzer/__main__.py`, `analyzer/fetch.py`, `tests/test_prices.py`, the README, and the Colab notebook in `notebooks/`.

**What he is responsible for.** The baseline algorithm for the best single buy and sell, and everything that gets the real data into the algorithms and shows the results.

**How the brute force works.** It builds a prefix-sum array of the daily price changes, then checks every start and end pair with one subtraction. There are n(n+1)/2 pairs (50,005,000 at 10,000 records), so the time is Œò(n¬≤) in the best, average and worst case, with Œò(n) extra space for the prefix array. When two windows earn the same profit, it keeps the earliest one. If every window loses money, it skips the trade and returns profit 0.

**How the data loading works.** `prices.py` reads the CSV and needs only three columns: `Ticker`, `Date` and `Adj Close`. Rows with a blank ticker, date or price are skipped. Each price is converted to an integer number of micro-dollars so all sums are exact, and prices are sorted by date for each ticker. The daily change is the difference between consecutive closes. Helper functions compute buy-and-hold return and map a window of changes back to a buy date and a sell date.

**The command-line tool.** `python3 -m analyzer --ticker AAPL --k 10` runs all three window algorithms and all three Top-K algorithms, times them, checks that they agree, and prints the best buy/sell window and the top K movers. `--html` writes a results page. `fetch.py` is an optional Yahoo Finance fallback that was not used for the paper or the benchmark.

**Results he can explain.**
- Brute force took 12.7 s at 10,000 records, against 2.9 ms for the linear scan (about 4,400 times slower).
- Its log-log slope from 1,000 to 10,000 records was 2.50, against the model value of 2.
- It was executed only through 10,000 records. The times at 100,000 and 1,000,000 records (21 minutes and 35 hours) are an n¬≤ projection from the 10,000-record median and were not measured.
- On AAPL all three algorithms agree: buy 2002-10-08 at $0.20, sell 2025-12-02 at $285.92.

**Resume bullets**
- Implemented a Œò(n¬≤) brute-force baseline for the best-buy/best-sell problem in Python and built the data pipeline and command-line tool that run it on 2.7 million rows of S&P 500 data.
- Measured 12.7 s at 10,000 records against 2.9 ms for a linear scan, fitted a log-log slope of 2.50 against the model value of 2, and projected 21 minutes at 100,000 and 35 hours at 1,000,000 records, labelled as projections and not measurements.

## Bhartendra Kumar Mandal: divide and conquer, benchmark runner, website generator

**Files:** `analyzer/max_subarray.py` (the divide-and-conquer functions), `analyzer/benchmark.py`, `tests/test_benchmark.py`, `benchmarks/results.json`, the figures in `docs/assets/`, and `docs/render.py`.

**What he is responsible for.** The Œò(n log n) window algorithm, and the experiments that compare all the algorithms across input sizes.

**How divide and conquer works.** It splits the array at the midpoint. The best window is entirely in the left half, entirely in the right half, or crosses the midpoint. The first two cases are the recursive calls. The crossing case is the best suffix of the left half plus the best prefix of the right half, and each is found with one linear scan. The recurrence is T(n) = 2T(n/2) + Œò(n), which the Master Theorem solves to Œò(n log n). Every input pays for the same scans, so the best, average and worst cases agree. Extra space is Œò(log n) for the recursion stack. Ties keep the earlier window, the same rule the other algorithms use.

**How the benchmark works.** It times prefixes of 1,000, 10,000, 100,000 and 1,000,000 records of the real data, five trials each, and reports the median. A second metric counts the work exactly: pair iterations, element reads, or comparisons. A memory trace records peak bytes. Brute force is executed only through 10,000 records; its larger times are fitted as c¬∑n¬≤ from the 10,000-record median and labelled as projected. For Top-K it times three arrangements of the input: market order, best case for the heap, and worst case for the heap. `render.py` turns `results.json` into the project website pages and the QR code.

**Results he can explain.**
- At 1,000,000 records divide and conquer takes 1.28 s, with log-log slope 1.04 from 10,000 to 1,000,000 records.
- A dry recursion counts exactly 20,951,424 element reads at one million records, which follows the n log n bound.
- Kadane (311 ms) is faster than divide and conquer in practice, even though both are efficient on paper, because each Python call in the recursion allocates a result.

**Resume bullets**
- Implemented the CLRS divide-and-conquer maximum-subarray algorithm, solved its recurrence T(n) = 2T(n/2) + Œò(n) with the Master Theorem, and checked it against the brute-force and Kadane implementations on the textbook example and on real data.
- Built the benchmark that times five trials at four input sizes up to one million records, counts operations exactly, and showed that divide and conquer performs 20,951,424 element reads at one million records and runs in 1.28 s.

## Aron Dardouri: Kadane's algorithm, Top-K, pseudocode

**Files:** `analyzer/max_subarray.py` (the `kadane` function), `analyzer/top_k.py`, `tests/test_top_k.py`, and `docs/algorithms.md`.

**What he is responsible for.** The linear-time window algorithm, the three Top-K algorithms, and the written pseudocode and correctness arguments.

**How Kadane works.** One left-to-right pass keeps a running sum. When the running sum becomes negative it is thrown away, because extending it cannot help any later window. The best window seen so far is updated whenever the running sum is positive. Time is Œò(n) in every case and extra space is Œò(1). Every correct algorithm has to read every entry, so the linear bound is tight for this problem.

**How the Top-K code works.** Items are ordered by higher score first, then by earlier ticker, so every algorithm returns the same list. The code includes three algorithms:
- **Full sort:** a merge sort written for the project, then the first K items. Œò(n log n) in every case, Œò(n) extra space.
- **Binary heap of size K:** a heap keeps the K best items seen so far, with the weakest at the root. A new item replaces the root only if it is better. Worst case Œò(n log k) when every item enters the heap, best case Œò(n + k log k) when the first K items are already the answer, and Œò(k) extra space.
- **Quickselect:** partitions around a pivot until the best K are in front. Œò(n) on average, Œò(n¬≤) in the worst case.
The merge sort and heap do not call `sorted()` or `heapq`. Those appear only in the tests as independent checkers.

**Pseudocode and correctness.** `docs/algorithms.md` has the pseudocode, the correctness arguments and the best, average and worst bounds for all six algorithms.

**Results he can explain.**
- Kadane takes 311 ms at 1,000,000 records, with log-log slope 1.01 from 1,000 to 1,000,000 records.
- On market order at one million records the size-10 heap takes 156 ms and 1,000,400 comparisons, against the full sort's 4.26 s and 18,638,382 comparisons.
- The heap's worst case (every item enters) costs 6,066,634 comparisons and 1.21 s, which shows the gap between its best and worst case.

**Resume bullets**
- Implemented Kadane's Œò(n) time, Œò(1) space algorithm for the best single buy and sell on 26 years of S&P 500 data, and showed it agrees with the brute-force and divide-and-conquer answers on every tested input.
- Wrote a merge sort, a size-K binary heap and quickselect for the Top-K problem, and measured the heap at 156 ms against 4.26 s for the full sort on one million records, with exact comparison counts for its best, typical and worst cases.

## Shared work

The technical paper and the presentation are still being prepared and will be added to the repository.

## Notes

- Brute force at 100,000 and 1,000,000 records is an n¬≤ projection from the 10,000-record median, not a measurement.
- Timings vary by machine and by run, especially the million-record sort. Re-run the benchmark before quoting them.

