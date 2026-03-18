from um import count

def test_count():
    assert count("umfeerf") == 0
    assert count("wvwfwf") == 0
    assert count("um,ecfece,um,umfcee") ==2
    assert count("um um um") == 3
    assert count("Um, thanks, um...") == 2
    