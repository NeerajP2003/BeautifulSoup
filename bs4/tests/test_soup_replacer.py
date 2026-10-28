from bs4 import BeautifulSoup, SoupReplacer


def test_replaces_matching_tag_during_parse():
    soup = BeautifulSoup(
        "<div><b>Important</b></div>",
        "html.parser",
        replacer=SoupReplacer("b", "blockquote"),
    )

    replacement = soup.blockquote
    assert replacement is not None
    assert replacement.get_text() == "Important"
    assert soup.find("b") is None


def test_replaces_all_matching_tags_and_closes_them():
    soup = BeautifulSoup(
        "<b>First</b><div><b>Second</b></div>",
        "html.parser",
        replacer=SoupReplacer("b", "blockquote"),
    )

    replacements = soup.find_all("blockquote")
    assert [tag.get_text() for tag in replacements] == ["First", "Second"]
    assert soup.div is not None
    assert soup.div.blockquote is not None
