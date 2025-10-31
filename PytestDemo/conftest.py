import pytest


@pytest.fixture(scope="class")
#fixture that is run before and after the function/class
def setup():
    print("first executed")
    yield
    print("last executed")

#data driven fixture to load the data
@pytest.fixture()
def daLoad():
    print("data are returned to the py test methods")
    return ["Mani", "mekalai", "mkalaianu@gmail.com"]

#parameterization of the data at fixture level
@pytest.fixture(params=[("chrome","mani"),("Edge", "mekalai")])
def crossBrowser(request):
    return request.param
