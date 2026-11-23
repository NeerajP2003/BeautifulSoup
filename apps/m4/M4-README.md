# Milestone-4

The goal of Milestone 4 is to make the BeautifulSoup object iterable so that users can directly iterate over all nodes in an HTML or XML document.

Implementation

Implemented the __iter__() method in bs4/__init__.py inside the BeautifulSoup class.

def __iter__(self) -> Iterator[PageElement]:
    """Iterate over all nodes in the document tree."""
    return self.descendants

The method returns the existing descendants iterator, which traverses the document tree and yields one node at a time.

No list of nodes is created or stored. This satisfies the assignment requirement to iterate through the tree without collecting its nodes into a list.

Usage

soup = BeautifulSoup(html_doc, "html.parser")

for node in soup:
    print(node)

Unit Tests

Five unit tests were added under TestSoupIteration in bs4/tests/test_soup.py:

test_empty_soup – Verifies iteration over an empty document.

test_single_tag – Verifies iteration over a document containing one tag.

test_nested_tags – Verifies traversal of nested tags and text nodes in document order.

test_text_nodes – Verifies that text nodes are included.

test_comments_and_sibling_tags – Verifies that comments and sibling tags are included.

Test Results

The complete BeautifulSoup test suite was executed using:

python -m pytest bs4/tests -q

Result: 634 passed, 216 skipped.
