import pytest


@pytest.mark.smoke
def test_firstpgm():
    print("first program in pytest")

@pytest.mark.smoke
def test_secondpgm():
    print("good morning")