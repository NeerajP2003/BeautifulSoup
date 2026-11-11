# Milestone 3: SoupReplacer API Brief

## Purpose

This brief compares the Milestone 2 and Milestone 3 `SoupReplacer` interfaces
and recommends how a future Beautiful Soup API could expose tag
transformations.

## Comparing the interfaces

Milestone 2 uses `SoupReplacer(old_tag, new_tag)`. It is small, readable, and
works well when the transformation is a single unconditional tag rename. Its
fixed pair is limiting when the replacement depends on a tag's name or
attributes, or when the transformation needs to change attributes as well as
the name.

Milestone 3 keeps that positional interface and adds three optional callbacks:

| Callback | Purpose | Result |
|---|---|---|
| `name_xformer(tag)` | Choose a tag name, potentially based on the tag | A replacement name, or `None` to keep the current name |
| `attrs_xformer(tag)` | Compute the tag's attributes | A replacement attribute mapping, or `None` to keep the current attributes |
| `xformer(tag)` | Make arbitrary changes to the tag | Mutate the tag; the return value is ignored |

Callbacks are applied to each tag as the parser creates it, in the order shown
above. When the legacy name pair and `name_xformer` are both supplied, the
callback receives the tag after the positional rename. Because the callbacks
run during parsing, they can transform tags without a separate pass over the
completed tree.

For example, conditional renaming and attribute cleanup can be expressed as:

```python
from bs4 import BeautifulSoup, SoupReplacer

def rename_bold_tags(tag):
    if tag.name == "b":
        return "blockquote"
    return tag.name

def remove_class(tag):
    attrs = dict(tag.attrs)
    attrs.pop("class", None)
    return attrs

replacer = SoupReplacer(
    name_xformer=rename_bold_tags,
    attrs_xformer=remove_class,
)
soup = BeautifulSoup(html_doc = "<b class='old'>Important</b>", "html.parser", replacer=replacer)
print(soup.prettify())
```

## Recommendation

I recommend retaining both interfaces. The positional pair is convenient for
the common, simple rename and should remain compatible with existing users.
The callback interface is a useful extension for conditional renaming,
attribute replacement, and tag-local mutations that would otherwise require
more custom code or a post-parse tree walk.

The callback API should be documented as an advanced option, with its callback
order, input tag state, return-value rules, and error behavior clearly
specified. In particular, callback exceptions should propagate rather than
being silently ignored. The API also introduces more complexity than a simple
rename: callbacks execute for every parsed tag, may affect parser-time state,
and their order can affect results. Keeping the positional form available
preserves a clear, low-complexity choice for simple use cases.

## Application: Milestone 1 task 7

[`task7.py`](./task7.py) reproduces task 7 by adding the class `test` to every
paragraph as it is parsed:

```shell
PYTHONPATH=. python apps/m3/task7.py input.html
```

The input path is required. The transformed document is written to
`modified_paragraphs.html` in the current working directory.
