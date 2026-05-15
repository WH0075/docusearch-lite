from src.docusearch.cleaner import clean_text

def test_clean_text_removes_extra_spaces():
    text = "hello      world"
    assert clean_text(text) == "hello world"

def test_clean_removes_extra_newlines():
    text = "hello\n\n\n\nworld"
    assert clean_text(text) == "hello\n\nworld"
