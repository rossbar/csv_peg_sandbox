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
