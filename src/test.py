import unittest
import validate_pin as pin
import persistent_bugger as burggers
import missing_letter as letter
import array_dif as diff

class TestUtils(unittest.TestCase):
    def test1(self):
        #Should return False for pins with length other than 4 or 6
        self.assertEqual(pin.validate_pin("1"), False, "Wrong output for '1'")
        self.assertEqual(pin.validate_pin("1"), False, "Wrong output for '1'")
        self.assertEqual(pin.validate_pin("12"), False, "Wrong output for '12'")
        self.assertEqual(pin.validate_pin("123"), False, "Wrong output for '123'")
        self.assertEqual(pin.validate_pin("12345"), False, "Wrong output for '12345'")
        self.assertEqual(pin.validate_pin("1234567"), False, "Wrong output for '1234567'")
        self.assertEqual(pin.validate_pin("-1234"), False, "Wrong output for '-1234'")
        self.assertEqual(pin.validate_pin("-12345"), False, "Wrong output for '-12345'")
        self.assertEqual(pin.validate_pin("1.234"), False, "Wrong output for '1.234'")
        self.assertEqual(pin.validate_pin("00000000"), False, "Wrong output for '00000000'")

        #Should return False for pins which contain characters other than digits
        self.assertEqual(pin.validate_pin("a234"),False, "Wrong output for 'a234'")
        self.assertEqual(pin.validate_pin(".234"),False, "Wrong output for '.234'")

        #Should return True for valid pins
        self.assertEqual(pin.validate_pin("1234"),True, "Wrong output for '1234'")
        self.assertEqual(pin.validate_pin("0000"),True, "Wrong output for '0000'")
        self.assertEqual(pin.validate_pin("1111"),True, "Wrong output for '1111'")
        self.assertEqual(pin.validate_pin("123456"),True, "Wrong output for '123456'")
        self.assertEqual(pin.validate_pin("098765"),True, "Wrong output for '098765'")
        self.assertEqual(pin.validate_pin("000000"),True, "Wrong output for '000000'")
        self.assertEqual(pin.validate_pin("123456"),True, "Wrong output for '123456'")
        self.assertEqual(pin.validate_pin("090909"),True, "Wrong output for '090909'")

    def test2(self):
        #Burgger test
        self.assertEqual(burggers.persistence(39), 3)
        self.assertEqual(burggers.persistence(4), 0)
        self.assertEqual(burggers.persistence(25), 2)
        self.assertEqual(burggers.persistence(999), 4)

    def test3(self):
       #Find_missing_letter tests
        self.assertEqual(letter.find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(letter.find_missing_letter(['O','Q','R','S']), 'P')

    def test4(self):
        #Fixed Tests
        self.assertEqual(diff.array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(diff.array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(diff.array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(diff.array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(diff.array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
        self.assertEqual(diff.array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

if __name__ == '__main__':
    unittest.main()



