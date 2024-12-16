import unittest
import Employee

class TestEmployee (unittest.TestCase):

    def setUp(self):
        self.employer = Employee

    def test_give_default_raise(self):
        self.assertEqual(self.employer.Employee("Ylia", "Lazareva", 5000).give_raise(0), 10000)

    def test_give_custom_raise(self):
        temp = int(input())
        self.assertEqual(self.employer.Employee("Ylia", "Lazareva", 5000).give_raise(temp), (5000+temp))

if __name__ == 'main':
    unittest.main()