import pytest


@pytest.mark.usefixtures("daLoad", "setup")
def test_getdata(daLoad): #since this fixture returns data, name of the fixture should be passed in method argument
    print(daLoad[0])
    print(daLoad[2])

@pytest.mark.usefixtures("crossBrowser")
def test_browserDetails(crossBrowser):
    print(crossBrowser[0])