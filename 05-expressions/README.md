# Expressions

An expression combines values, variables, and operators to produce a value.
For example, `price * quantity` evaluates to a number.

This folder currently contains this reference guide rather than a Python
script. Try the examples in a Python file or interactive prompt.

## Common operators

| Kind | Operators | Example |
| --- | --- | --- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `7 // 2` is `3` |
| Comparison | `==`, `!=`, `<`, `<=`, `>`, `>=` | `age >= 18` |
| Logical | `and`, `or`, `not` | `is_ready and has_ticket` |

`/` performs division and returns a float. `//` gives a floor-division result,
`%` gives the remainder, and `**` raises a number to a power. Comparisons
produce `True` or `False`.

Python follows operator precedence. Use parentheses to make the intended
grouping clear:

```python
total = (price + tax) * quantity
is_adult = age >= 18
```

## Additional notes

- `=` assigns a value; `==` compares two values for equality.
- `and`, `or`, and `not` combine or invert truth values. `and` and `or`
  short-circuit: Python may not evaluate the right-hand expression if the
  result is already determined.
- `+` can add numbers or concatenate strings. Operators behave according to
  the types of their operands.
- Division by zero raises `ZeroDivisionError`.
- Parentheses can clarify grouping even when they are not strictly required.

Try changing the arithmetic and comparison operators in
[`01-fundamentals/variables-and-data-types.py`](../01-fundamentals/variables-and-data-types.py).
