# Trying PEG parsing for CSV files

See: https://textx.github.io/Arpeggio/stable/tutorials/csv/

### Notes

The PEG parser appears to consume quite a bit of memory.
For example, a csv file containing `10k x 5` array of `1.2%f` formatted floats
results in a 40 MB PEG tree object at the intermediate parsing step (i.e.
before the data is extracted into an ndarray).
Compare this with the ~1.3 MB used by `np.loadtxt` during line-by-line parsing.

To reproduce:

```
python -m memory_profiler peg_csv.py
```

The `arpeggio.PythonParser.parse` method is also significantly slower than
even the Python implementation of `np.loadtxt`.
This doesn't necessarily mean that PEG parsing itself isn't performant, but the
lack of performance makes it cumbersome to do parametric studies (i.e.
memory usage vs. file size or data format) for data files of reasonable size.

For example, on my system:

```
In [1]: fname = "testdata_float64_10000x5.csv"  # Generated in above step

In [2]: from peg_csv import parser

In [3]: import numpy as np

In [4]: %timeit parser.parse_file(fname)
817 ms ± 1.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [5]: %timeit np.loadtxt(fname, delimiter=",")
37.8 ms ± 340 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```
