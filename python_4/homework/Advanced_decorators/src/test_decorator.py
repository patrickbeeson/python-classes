import unittest
from decorator import addarg

@addarg("tiger ")
def concat(*strings, **kwargs):
    output = ""
    for element in strings:
        output += element
    if "uppercase" in kwargs:
        if kwargs["uppercase"]:  # uppercase = True passed as keyword argument
            output = output.upper()
    return output

class TestDecorator(unittest.TestCase):
    
    def test_concat(self):
        observed = concat("tiger ", "burning ", "bright")
        expected = "tiger tiger burning bright"
        self.assertEqual(observed, expected, "Not the same")

    def test_concat2(self):
        observed = concat("tiger ", "burning ", "bright", uppercase=True)
        expected = "TIGER TIGER BURNING BRIGHT"
        self.assertEqual(observed, expected, "Not the same")

    def test_decorator_adds_argument_to_function(self):
        @addarg(1)
        def prargs(*args):
            return args
        expected = (1, 2, 3)
        observed = prargs(2, 3)
        self.assertEqual(expected, observed)

    def test_decorator_no_arguments(self):
        @addarg(1)
        def prargsnone(*args):
            return args
        expected = (1,)
        observed = prargsnone()
        self.assertEqual(expected, observed)

    
if __name__ == "__main__":
    unittest.main()
