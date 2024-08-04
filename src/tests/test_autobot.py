import unittest
import autobot


class MyTestCase(unittest.TestCase):
    def test_something(self):
        @autobot.task(depends=goodbye)
        def hello_there():
            pass

        autobot.run_all()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
