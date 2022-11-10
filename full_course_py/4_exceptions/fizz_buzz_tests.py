import unittest
import fizz_buzz


class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        """
        test fizz
        :return: TEST
        """
        number: int = 6

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        """
        test buzz
        :return:  TEST
        """
        number: int = 10

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'Buzz')

    def test_fizz_buzz(self):
        """
        test_fizz_buzz
        :return: TEST
        """
        number: int = 15

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 'FizzBuzz')

    def test_number(self):
        """
        test_fizz_buzz
        :return: TEST
        """
        number: int = 13

        result = fizz_buzz.get_reply(number)

        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()