import unittest

class MyTestPedro(unittest.TestCase):
    def test_pedro(self):
        data = "Pedro"
        self.assertEqual(data, "Pedro")
        
if __name__ == '__main__':
    unittest.main()
