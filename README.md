# Python Learning Notes

A beginner-friendly collection of short Python examples and exercises. Each
script can be run on its own; this repository is a learning project, not an
installable Python package.

## Learning path

Work through the numbered folders in order:

1. [`01-fundamentals/`](./01-fundamentals/) - [lesson notes](./01-fundamentals/README.md) on variables, data types, input, and type conversion
2. [`02-strings/`](./02-strings/) - [lesson notes](./02-strings/README.md) on string creation, indexing, slicing, and methods
3. [`03-collections/`](./03-collections/) - [lesson notes](./03-collections/README.md) on lists, tuples, dictionaries, and sets
4. [`04-modules/`](./04-modules/) - [lesson notes](./04-modules/README.md) on imports, standard-library modules, and an external package
5. [`05-expressions/`](./05-expressions/) - [operator notes](./05-expressions/README.md) on arithmetic, comparison, and logical expressions
6. [`06-loops/`](./06-loops/) - [lesson notes](./06-loops/README.md) on `for`, `while`, and controlling loops
7. [`07-exercises/`](./07-exercises/) - [practice notes](./07-exercises/README.md) for collections and loops
8. [`08-Function/`](./08-Function/) - [lesson notes](./08-Function/README.md) on functions and recursion

## Getting started

Install Python 3. The examples mostly use the standard library. The
`pyjokes-example.py` script is the only one that needs the optional `pyjokes`
package listed in `requirements.txt`.

Create and activate a virtual environment from the repository folder:

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the optional package only if you want to run the joke example:

```bash
python -m pip install -r requirements.txt
```

## Run an example

Run commands from the repository root so the paths below work:

```bash
python 02-strings/strings.py
python 06-loops/for-loop.py
python 08-Function/function.py
python 08-Function/recursion.py
```

On Windows, use `py` instead of `python` if that is how Python is installed.
Some scripts ask for input; follow the prompts in the terminal.

## Learning notes

- Read the comments in each script, then change a value and run it again.
- The scripts are independent examples; there is no test suite or build step.
- If an example behaves unexpectedly, include the command you ran and the
  Python version when opening an issue.
- See [`05-expressions/README.md`](./05-expressions/README.md) for a quick
  operator reference and [`07-exercises/README.md`](./07-exercises/README.md)
  for practice suggestions. The [`08-Function/README.md`](./08-Function/README.md)
  covers functions and recursion.

## Contributing

Small beginner-friendly improvements are welcome. Keep examples focused, add
comments where they clarify a concept, and update this learning path when
adding or moving lessons. For larger changes, open an issue first to discuss
the proposed lesson.

## License

This repository does not currently include a license. Choose and add a license
before inviting others to reuse or redistribute its contents.
