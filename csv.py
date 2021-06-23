from arpeggio import ZeroOrMore, OneOrMore, EOF, ParserPython
from arpeggio import RegExMatch as rem

# Define grammar from tutorial:
# https://textx.github.io/Arpeggio/stable/tutorials/csv/#the-grammar
def record():
    return field, ZeroOrMore(",", field)


def field():
    return [quoted_field, field_content]


def quoted_field():
    return '"', field_content_quoted, '"'


def field_content():
    return rem(r'([^,\n])+')


def field_content_quoted():
    return rem(r'(("")|([^"]))+')


def csvfile():
    return OneOrMore([record, '\n']), EOF


parser = ParserPython(csvfile, ws='\t ')


if __name__ == "__main__":
    import numpy as np

    # Generate test data
    rng = np.random.default_rng()
    a = rng.random((1000, 5))
    fname = f"testdata_{a.dtype}_{a.shape[0]}x{a.shape[1]}.csv"
    np.savetxt(fname, a, fmt="%.2f", delimiter=",")

    # Parse test data
    with open(fname, 'r') as fh:
        test_data = fh.read()
    parse_tree = parser.parse(test_data)
