# Milestone 2

## Part 2: Beautiful Soup API source references

The references below point to the Beautiful Soup source files in this
repository. Line numbers identify the start of each definition in the
provided source; they should be checked against the original source before
making any Part 3 changes.

### APIs used in Milestone 2 Part 1

| API used | Used in | Definition in Beautiful Soup source |
|---|---|---|
| `BeautifulSoup(...)` constructor | `task2.py`, `task3.py`, `task4.py` | [`bs4/__init__.py`, line 209](../../bs4/__init__.py#L209) |
| `SoupStrainer(...)` constructor | `task2.py`, `task3.py`, `task4.py` | [`bs4/filter.py`, line 345](../../bs4/filter.py#L345) |
| `Tag.find_all(...)` | `task2.py`, `task3.py`, `task4.py` | [`bs4/element.py`, line 2715](../../bs4/element.py#L2715) |

`BeautifulSoup` is given the `SoupStrainer` through its `parse_only`
argument. The three programs use these filters:

| Program | `SoupStrainer` filter |
|---|---|
| `task2.py` | `SoupStrainer("a")` selects anchor tags. |
| `task3.py` | `SoupStrainer(True)` matches all tags, so it demonstrates `SoupStrainer` but does not reduce the parsed tag set. |
| `task4.py` | `SoupStrainer(attrs={"id": True})` selects tags with an `id` attribute. |

### APIs used in Milestone 1

| API used | Used in | Definition in Beautiful Soup source |
|---|---|---|
| `BeautifulSoup(...)` constructor | `task2.py`, `task3.py`, `task4.py` | [`bs4/__init__.py`, line 209](../../bs4/__init__.py#L209) |
| `Tag.find_all(...)` | `task2.py`, `task3.py`, `task4.py` | [`bs4/element.py`, line 2715](../../bs4/element.py#L2715) |

The Milestone 1 programs use `find_all(True)` in task 2 to select all tags,
`find_all(id=True)` in task 3 to select tags with an `id` attribute, and
`find_all("a")` in task 4 to select anchor tags. They all construct the soup
with the `"html.parser"` parser.
