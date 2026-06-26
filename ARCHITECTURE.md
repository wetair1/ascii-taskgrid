# Architecture

ascii-taskgrid is a small curses task board built with the Python standard library.

## Runtime flow

1. Tasks are loaded from a JSON file in the user's home directory.
2. The curses UI renders the current task list.
3. Keyboard input changes selection, toggles completion, adds tasks or deletes tasks.
4. Tasks are saved back to disk when the user exits or changes data.
5. Pressing `q` exits the app.

## Main parts

- `load_tasks()` reads the local JSON task database.
- `save_tasks()` writes task data back to disk.
- `prompt()` captures text input inside curses.
- `app()` owns rendering, keyboard controls and state changes.

## Design rules

- Keep dependencies at zero.
- Store data in a simple human-readable format.
- Keep key bindings small and memorable.
- Keep rendering separate from persistence helpers.
- Avoid surprising writes outside the user's home directory.
