from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_ums():
    assert count("Um, well, um... I don't know, UM maybe?") == 3

def test_um_inside_words():
    assert count("yummy umbrella thumper") == 0

def test_um_mixed_with_punctuation():
    assert count("Um! Is that you, um? No UM.") == 3

def test_case_insensitivity():
    assert count("UM um Um uM") == 4
