from typing import Any, Callable, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from bs4.element import Tag


class SoupReplacer:
    """Transform tags as they are created during parsing.

    Two positional arguments retain the original API: the old tag name and
    its replacement. The keyword callbacks provide more flexible transforms.
    """

    def __init__(
        self,
        *args: str,
        name_xformer: Optional[Callable[["Tag"], Optional[str]]] = None,
        attrs_xformer: Optional[
            Callable[["Tag"], Optional[Dict[str, Any]]]
        ] = None,
        xformer: Optional[Callable[["Tag"], None]] = None,
    ) -> None:
        if len(args) == 2:
            self.old_tag, self.new_tag = args
        elif args:
            raise TypeError(
                "SoupReplacer accepts either zero or two positional arguments"
            )
        else:
            self.old_tag = None
            self.new_tag = None

        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def replacement_name(self, name: str) -> str:
        """Return the legacy positional replacement for a tag name."""
        if (
            self.old_tag is not None
            and self.new_tag is not None
            and name == self.old_tag
        ):
            return self.new_tag
        return name

    def transform_tag(self, tag: "Tag") -> None:
        """Apply configured transformations to a newly-created tag."""
        if self.name_xformer is not None:
            replacement_name = self.name_xformer(tag)
            if replacement_name is not None:
                tag.name = replacement_name

        if self.attrs_xformer is not None:
            replacement_attrs = self.attrs_xformer(tag)
            if replacement_attrs is not None:
                attrs = dict(replacement_attrs)
                tag.attrs.clear()
                tag.attrs.update(attrs)

        if self.xformer is not None:
            self.xformer(tag)
