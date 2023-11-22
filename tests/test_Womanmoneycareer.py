from Womanmoneycareer.Womanmoneycareer import Womanmoneycareer

def test_multiply():
    assert Womanmoneycareer.multiply(2, 3) == 6
from Womanmoneycareer import Womanmoneycareer

def test_multiply():
    assert Womanmoneycareer.multiply(2, 3) == 6

def test_hello():
    # Test case 1: Check if the function returns the correct greeting
    assert Womanmoneycareer.hello("Alice") == "Hello, Alice!"

    # Test case 2: Check if the function returns the correct greeting for an empty string
    assert Womanmoneycareer.hello("") == "Hello, !"

    # Test case 3: Check if the function returns the correct greeting for a name with special characters
    assert Womanmoneycareer.hello("@#$%^") == "Hello, @#$%^!"
