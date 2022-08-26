import unittest
import decoratorExample

class test_decorator(unittest.TestCase):
    def test_decorator_add(self):
        print('---------testing decorator add function-------------')
        add = decoratorExample.iden(decoratorExample.add)
        print(add(3, 4))



if __name__ == '__main__':
    unittest.main()
