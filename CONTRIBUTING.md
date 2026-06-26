# Contributing

Thanks for improving ascii-taskgrid.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-taskgrid.git
cd ascii-taskgrid
python3 main.py
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Keep data storage simple and transparent.
- Keep key bindings documented.
- Keep the TUI usable on small terminals.
- Save user data safely.

## Checks

```bash
python3 -m py_compile main.py
python3 main.py
```

## Commit style

Use short imperative messages, for example:

- `Add task editing`
- `Fix save handling`
- `Document controls`
