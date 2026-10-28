# Loops

The [`for-loop.py`](./for-loop.py) script demonstrates `for` and `while`
loops, accumulation, and exiting a loop early. Run it from the repository
root:

```bash
python 06-loops/for-loop.py
```

## Key notes

- A `for` loop visits each item in an iterable, such as a list, string, or
  `range`. Use it when iterating over items or a known sequence of values.
- `range(start, stop, step)` generates integers; the `stop` value is excluded.
  For example, `range(1, 6)` produces `1, 2, 3, 4, 5`.
- A `while` loop repeats as long as its condition is true. Update the state
  used by the condition so the loop can eventually finish.
- Indentation defines the loop body. Statements at the same indentation level
  execute together on each iteration.
- `break` exits the nearest loop. `continue` skips to its next iteration.
- An accumulator, such as `sum_value`, can collect a result across iterations.
- If a `while` condition never becomes false and the loop never exits, the
  program can run indefinitely.

The script contains finite examples; change loop bounds cautiously so each
example still terminates.
