#!/usr/bin/env python3
import curses
import json
import os

TASK_FILE = os.path.expanduser('~/.ascii_taskgrid.json')


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)


def prompt(stdscr, text):
    curses.echo()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h - 1, 0, ' ' * (w - 1))
    stdscr.addstr(h - 1, 0, text)
    value = stdscr.getstr(h - 1, len(text), w - len(text) - 1).decode().strip()
    curses.noecho()
    return value


def app(stdscr):
    curses.curs_set(0)
    tasks = load_tasks()
    selected = 0

    while True:
        h, w = stdscr.getmaxyx()
        stdscr.erase()
        stdscr.addstr(0, 2, 'ASCII TASKGRID - a add, space done, d delete, q quit')
        cols = max(1, min(3, w // 28))
        card_w = max(20, w // cols - 2)

        for idx, task in enumerate(tasks[: max(1, (h - 3) * cols)]):
            row = 2 + (idx // cols) * 3
            col = 2 + (idx % cols) * card_w
            mark = 'x' if task.get('done') else ' '
            cursor = '>' if idx == selected else ' '
            title = task.get('title', '')[: card_w - 8]
            stdscr.addstr(row, col, '+' + '-' * (card_w - 4) + '+')
            stdscr.addstr(row + 1, col, f'|{cursor}[{mark}] {title:<{card_w - 9}}|')
            stdscr.addstr(row + 2, col, '+' + '-' * (card_w - 4) + '+')

        ch = stdscr.getch()
        if ch in (ord('q'), ord('Q')):
            save_tasks(tasks)
            break
        if ch in (curses.KEY_RIGHT, ord('l')) and selected < len(tasks) - 1:
            selected += 1
        if ch in (curses.KEY_LEFT, ord('h')) and selected > 0:
            selected -= 1
        if ch in (curses.KEY_DOWN, ord('j')):
            selected = min(len(tasks) - 1, selected + cols)
        if ch in (curses.KEY_UP, ord('k')):
            selected = max(0, selected - cols)
        if ch == ord('a'):
            title = prompt(stdscr, 'new task: ')
            if title:
                tasks.append({'title': title, 'done': False})
                selected = len(tasks) - 1
        if ch == ord(' ') and tasks:
            tasks[selected]['done'] = not tasks[selected].get('done')
        if ch == ord('d') and tasks:
            tasks.pop(selected)
            selected = max(0, min(selected, len(tasks) - 1))


if __name__ == '__main__':
    curses.wrapper(app)
