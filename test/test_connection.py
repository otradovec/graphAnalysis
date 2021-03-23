import unittest
from src.Connection import Connection

class ConnectionTest(unittest.TestCase):
    def test_connection_equality(self):
        f = "A"
        t = "B"
        o = True
        self.assertEqual(Connection(f,t,o),Connection(f,t,o))

if __name__ == '__main__':
    unittest.main()
