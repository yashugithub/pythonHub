import unittest
import sequenceMean

class seq_test(unittest.TestCase):
    def test_seq(self):
        result = sequenceMean.seqMean([1,2,3,4])
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()

