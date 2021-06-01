# Rewrite this in Unit Test
import unittest
from caesar_cipher import caesar_cipher
class CaesarCipherTestCase(unittest.TestCase):

    def test_case_1(self):
        output = caesar_cipher("Boy! What a string!", -5)
        self.assertEqual(output, "Wjt! Rcvo v nomdib!")

    def test_case_2(self):
        output = caesar_cipher("Hello zach168! Yes here.", 5)
        self.assertEqual(output, "Mjqqt efhm168! Djx mjwj.")
    
    def test_case_3(self):
        output = caesar_cipher("Hello zach168! Yes here.", -5)
        self.assertEqual(output, "Czggj uvxc168! Tzn czmz.")

if __name__ == '__main__':
    unittest.main()