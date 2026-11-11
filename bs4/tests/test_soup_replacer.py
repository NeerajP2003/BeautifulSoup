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


def test_name_xformer_replaces_tags_and_closes_original_names():
    soup = BeautifulSoup(
        "<b><i>First</i></b><b>Second</b>",
        "html.parser",
        replacer=SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        ),
    )

    replacements = soup.find_all("blockquote")
    assert [tag.get_text() for tag in replacements] == ["First", "Second"]
    assert soup.find("b") is None


def test_name_xformer_leaves_unmatched_names_unchanged():
    soup = BeautifulSoup(
        "<b>Bold</b><i>Italic</i>",
        "html.parser",
        replacer=SoupReplacer(
            name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name
        ),
    )

    assert soup.strong is not None
    assert soup.i is not None
    assert soup.b is None


def test_attrs_xformer_replaces_attributes():
    def replace_attributes(tag):
        return {"id": tag.get("id"), "data-kind": "converted"}

    soup = BeautifulSoup(
        '<p id="one" class="old">Text</p>',
        "html.parser",
        replacer=SoupReplacer(attrs_xformer=replace_attributes),
    )

    paragraph = soup.p
    assert paragraph is not None
    assert paragraph.attrs == {"id": "one", "data-kind": "converted"}


def test_xformer_mutates_tags_as_they_are_parsed():
    def add_class(tag):
        if tag.name == "p":
            tag["class"] = "test"

    soup = BeautifulSoup(
        "<div><p>First</p><p class='old'>Second</p></div>",
        "html.parser",
        replacer=SoupReplacer(xformer=add_class),
    )

    assert [tag["class"] for tag in soup.find_all("p")] == ["test", "test"]


def test_transformers_run_in_name_attributes_and_side_effect_order():
    calls = []

    def transform_name(tag):
        calls.append(("name", tag.name))
        return "section"

    def transform_attrs(tag):
        calls.append(("attrs", tag.name))
        return {"data-name": tag.name}

    def transform_tag(tag):
        calls.append(("xformer", tag.name, tag.get("data-name")))
        tag["data-ready"] = "yes"

    soup = BeautifulSoup(
        "<div>Text</div>",
        "html.parser",
        replacer=SoupReplacer(
            name_xformer=transform_name,
            attrs_xformer=transform_attrs,
            xformer=transform_tag,
        ),
    )

    assert calls == [
        ("name", "div"),
        ("attrs", "section"),
        ("xformer", "section", "section"),
    ]
    assert soup.section is not None
    assert soup.section["data-ready"] == "yes"


def test_name_xformer_handles_self_closing_tags():
    soup = BeautifulSoup(
        "<b/>after<b>inside</b>",
        "html.parser",
        replacer=SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        ),
    )

    replacements = soup.find_all("blockquote")
    assert len(replacements) == 2
    assert replacements[0].get_text() == ""
    assert replacements[1].get_text() == "inside"
    assert soup.get_text() == "afterinside"
