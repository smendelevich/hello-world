from hello import greet


def test_normal_name():
    assert greet("Alice") == "Hello, Alice!"


def test_empty_string():
    assert greet("") == "Hello, World!"


def test_hebrew_name():
    assert greet("שירה") == "Hello, שירה!"


def test_name_with_extra_spaces():
    assert greet("  Bob  ") == "Hello, Bob!"
