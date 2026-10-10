# Python practice applications

Small interactive exercises using Python's standard library. Data is held in memory and resets when the program exits.

| File | Purpose |
| --- | --- |
| `student gradebook.py` | Add students and look up grades by name |
| `to do list final.py` | Add, remove, and view tasks |
| `to_do_list.py` | Practice a repeating yes/no input loop |

## Run

Requires Python 3; no external packages. Quote filenames containing spaces:

```sh
python "student gradebook.py"
python "to do list final.py"
python to_do_list.py
```

Use `exit` to leave the gradebook or task list. The original `exist` command also works for compatibility. Removing an unknown task reports that it was not found.

Existing PyCharm settings are preserved; `.gitignore` excludes new local settings and Python caches.
