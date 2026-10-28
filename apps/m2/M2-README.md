# Milestone 2

## Part 2: Beautiful Soup API source references

The references below use line numbers from the original Beautiful Soup
source in the repository's initial commit (`HEAD`), before the Part 3
changes.

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
| `task2.py` | `SoupStrainer(True)` selects all tags, matching Milestone 1 task 2. Since every tag is needed, this filter cannot reduce the parsed tag set. |
| `task3.py` | `SoupStrainer(attrs={"id": True})` selects tags with an `id` attribute, matching Milestone 1 task 3. |
| `task4.py` | `SoupStrainer("a")` selects anchor tags, matching Milestone 1 task 4. |

### APIs used in Milestone 1

| API used | Used in | Definition in Beautiful Soup source |
|---|---|---|
| `BeautifulSoup(...)` constructor | tasks 2, 3, 4, 6, 7 | [`bs4/__init__.py`, line 209](../../bs4/__init__.py#L209) |
| `Tag.find_all(...)` | tasks 2, 3, 4, 6, 7 | [`bs4/element.py`, line 2715](../../bs4/element.py#L2715) |
| `Tag.name` setter | task 6 (`tag.name = "blockquote"`) | [`bs4/element.py`, line 1354](../../bs4/element.py#L1354) |
| `Tag.__setitem__(...)` | task 7 (`tag["class"] = "test"`) | [`bs4/element.py`, line 2223](../../bs4/element.py#L2223) |
| `Tag.prettify(...)` | tasks 6, 7 | [`bs4/element.py`, line 2601](../../bs4/element.py#L2601) |

The Milestone 1 programs provided for tasks 2, 3, and 4 use `find_all(True)`
to select all tags, `find_all(id=True)` to select tags with an `id`
attribute, and `find_all("a")` to select anchor tags, respectively. Tasks 6
and 7 additionally rename a tag and set its `class` attribute before calling
`prettify()`.

The assignment text says "two application programs" but names three tasks;
this submission has a separate program for each task.

### Part 1 large-file test

The original `large_test.html` file was no longer present, so the three
programs were tested against a generated temporary HTML file of 3,397,292
bytes. The fixture contained 100,000 ordinary `div` tags and occasional
paragraphs with `id` attributes and links. Output was redirected to
`/dev/null` during timing.

| Program | Result | Elapsed time |
|---|---|---:|
| `task2.py` | Completed; selected all tags as required. | 11.64 s |
| `task3.py` | Completed; selected ID-bearing tags. | 2.39 s |
| `task4.py` | Completed; selected links. | 2.24 s |

Task 2 necessarily parses all tags because its Milestone 1 operation asks for
all tags; the `SoupStrainer` is used, but cannot reduce the amount parsed for
that task. The generated fixture was temporary and was removed after testing.
