import unittest
from context_mgr import Context

class TestContextManager(unittest.TestCase):

    def test_raises_exception(self):
        "Test should raise TypeError exception"
        with self.assertRaises(TypeError):
            with Context():
                raise TypeError

    def test_supresses_valueerror(self):
        "Test shouldn't raise ValueError exception"
        with Context():
            raise ValueError

if __name__ == "__main__":
    unittest.main()
