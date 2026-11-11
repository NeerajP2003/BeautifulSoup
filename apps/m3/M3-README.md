# Milestone 3: SoupReplacer API Recommendation

## API comparison

Milestone 2's `SoupReplacer(old_tag, new_tag)` is compact and easy to learn.
It is a good fit for a single unconditional tag-name substitution, but it
cannot make decisions based on a tag's attributes or content, transform
attributes, or perform arbitrary tag-local changes. Its meaning is also
limited to a fixed pair of names.

Milestone 3 keeps that positional form for compatibility and adds optional
`name_xformer`, `attrs_xformer`, and `xformer` callbacks. The first two return
replacement values; `xformer` can mutate the newly-created tag and is useful
for side effects. This supports conditional renaming, attribute cleanup, and
other transformations during parsing instead of requiring a second tree walk.
The callbacks run in name, attributes, then side-effect order.

## Recommendation

I recommend keeping both interfaces, with the callback API as the preferred
extension point for new transformations. The legacy positional form remains
more discoverable for simple renames and avoids breaking existing callers.
The callback interface is more expressive without requiring a separate
subclass for each transformation. The contract should remain explicit:
callbacks receive each parsed tag, name and attribute callbacks return the
replacement value (or `None` to leave it unchanged), and the side-effect
callback should mutate the tag without relying on a return value. Callback
exceptions should propagate so a failed transformation is not silently hidden.

## Example application

[`task7.py`](./task7.py) reproduces Milestone 1 task 7: it adds the class
`test` to every paragraph during parsing, using `SoupReplacer(xformer=...)`.
Run it with an HTML file path:

```shell
PYTHONPATH=. python apps/m3/task7.py input.html
```

The transformed document is written to `modified_paragraphs.html`.
