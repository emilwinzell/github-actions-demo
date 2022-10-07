from hello import add, mod


def test_add():
    assert 2 == add(1, 1)

def test_mod():
    assert 4 == mod(9,5)
