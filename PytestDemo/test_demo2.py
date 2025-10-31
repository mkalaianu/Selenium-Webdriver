import pytest


@pytest.mark.skip
#@pytest.mark.xfail
def test_firstpgm():
    msg = "Hello"
    assert msg == "hi", "strings are not same"


def test_secondfile():
    a=2
    b=6
    assert a+4 == b, "Addition does not match"
