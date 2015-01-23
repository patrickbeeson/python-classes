import unittest
from inspect import ismodule, getmembers, isfunction
from findfunc import FuncFinder


class TestFindFunc(unittest.TestCase):
    def setUp(self):
        import json
        self.funccount = len(getmembers(json, isfunction))
        self.funcfinder = FuncFinder('json')

    def test_imports_module(self):
        "Test our module is imported"
        expected = True
        observed = ismodule(self.funcfinder.module)
        self.assertEqual(observed, expected)

    def test_find_functions(self):
        "Test whether we get an accurate count of functions from module"
        expected = self.funccount
        observed = self.funcfinder.func_lst
        self.assertEqual(expected, len(observed))

    def test_module_output(self):
        "Test one line of generator output for a match"
        observed = ['{}'.format(func) for func in self.funcfinder.get_funclst_argspec()][0]
        expected = 'def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)'
        self.assertEqual(expected, ''.join(observed))


if __name__ == "__main__":
    unittest.main()