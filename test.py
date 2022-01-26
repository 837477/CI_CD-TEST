from unittest import TestCase, main

class MyTest(TestCase):
    def test_sum(self):
        self.assertEqual(1+2, 3)
    
    def test_sub(self):
        self.assertEqual(2-1, 0)

if __name__ == "__main__":
    main(verbosity=2)