# Fundamentals

These lessons introduce values, variables, basic types, conversion, and
terminal input. Run them from the repository root:

```bash
python 01-fundamentals/variables-and-data-types.py
python 01-fundamentals/type-casting.py
python 01-fundamentals/input-and-addition.py
```

## Key notes

- A variable name refers to a value. Use descriptive names such as `age` or
  `total` and follow Python's `snake_case` convention.
- Common built-in types include `int` (whole numbers), `float` (decimal
  numbers), `str` (text), and `bool` (`True` or `False`).
- `input()` always returns text. Convert it before doing numeric calculations:
  `int(input(...))` for whole numbers or `float(input(...))` for decimals.
- Conversion can fail if the text is not a valid number; for example,
  `int("hello")` raises `ValueError`.
- Converting a float with `int()` truncates the fractional part toward zero;
  it does not round to the nearest integer.
- `print()` displays values. `type(value)` can help inspect a value's type.

The addition example expects two whole-number inputs. Try decimal values by
changing the conversions to `float()`.
