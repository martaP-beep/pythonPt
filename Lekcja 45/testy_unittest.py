import unittest
import funkcje

class TestFunkcje(unittest.TestCase):

    def test_dodaj(self):
        self.assertEqual(funkcje.dodaj(2,3), 2+3)
    
    def test_palindrom(self):
        self.assertEqual(funkcje.czy_palindrom("oko"), True)
        self.assertTrue(funkcje.czy_palindrom("zez"))




if __name__ == "__main__":
    unittest.main() 