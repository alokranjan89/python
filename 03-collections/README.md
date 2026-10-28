# Collections

This folder introduces lists, tuples, dictionaries, and sets. Run the examples
from the repository root:

```bash
python 03-collections/lists-and-tuples.py
python 03-collections/dictionary-sets.py
```

## Choosing a collection

| Collection | Ordered | Mutable | Main use |
| --- | --- | --- | --- |
| `list` | Yes | Yes | A sequence that may change |
| `tuple` | Yes | No | A fixed sequence of values |
| `dict` | Insertion ordered | Yes | Key-value lookups |
| `set` | No positional order | Yes | Unique values and membership checks |

## Key notes

- Lists use `[]`; access items by index. Methods such as `.append()` change the
  list in place. `.pop()` removes and returns an item.
- Tuples use `()`. A one-item tuple needs a trailing comma, as in `(7,)`.
- Dictionaries map unique, hashable keys to values. Use `.get(key)` when a
  missing key should return `None` instead of raising `KeyError`.
- Sets contain unique, hashable values. Use `set()` for an empty set; `{}` is
  an empty dictionary.
- Set union (`|`), intersection (`&`), difference (`-`), and symmetric
  difference (`^`) compare groups of values.
- A set does not guarantee a display order. Do not rely on the order printed
  by the examples.
- `20` and `20.0` compare equal, so a set stores only one of them; `"20"` is a
  string and is a distinct value.

The examples modify some collections as they run. Re-run a script to start
again with its original values.
