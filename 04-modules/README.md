# Modules

A module is a Python file or library that provides reusable code. Run the
external-package example from the repository root:

```bash
python 04-modules/pyjokes-example.py
```

## Module types

- **Standard library:** included with Python; examples include `math`, `random`,
  and `pathlib`. Import a module with `import math`, then use names such as
  `math.sqrt(9)`.
- **Third-party package:** installed separately, usually with `pip`. The
  `pyjokes-example.py` script imports the third-party `pyjokes` package.
- **Your own module:** another `.py` file in a project that you import and
  reuse.

Install the optional third-party dependency from the project root:

```bash
python -m pip install -r requirements.txt
```

`modules-overview.py` is a short concept note. The examples in
`standard-library-examples.py` are currently commented out, so they do not run
until you uncomment one. The commented `os.listdir()` examples inspect the
filesystem; use a directory path that exists on your own computer.

Prefer `pathlib.Path` for portable filesystem paths. Avoid copying a
machine-specific absolute path from an example without adapting it.
