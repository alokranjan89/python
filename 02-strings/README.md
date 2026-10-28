# Strings

The [`strings.py`](./strings.py) script demonstrates common string operations.
Run it from the repository root:

```bash
python 02-strings/strings.py
```

## Key notes

- Strings hold text and can use single, double, or triple quotes.
- Indexing starts at `0`; negative indexes count from the end. An index that
  is outside the string raises `IndexError`.
- A slice has the form `text[start:stop:step]`. The `stop` position is
  excluded; omitted values use defaults. A step of `-1` reverses the text.
- Strings are immutable. Methods such as `.upper()` and `.replace()` return
  new strings; they do not change the original string.
- `.strip()` removes whitespace at the ends, `.split()` makes a list, and
  `.join()` combines strings from an iterable.
- Use f-strings, such as `f"Hello, {name}"`, to include values in text.
- `in` checks whether a substring exists. `.find()` returns `-1` when a
  substring is not found.
- Methods such as `.isalpha()` and `.isdigit()` check character categories;
  they do not convert the string to another type.

Try changing the sample text and predicting each output before running the
script.
