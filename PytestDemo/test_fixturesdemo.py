import pytest


@pytest.mark.usefixtures("setup")
class TestMultiplePrograms:

    def test_firstpgm(self):
        print("first program")

    def test_secondpgm(self):
        print("second program")

    def test_thirdpgm(self):
        print("third program")