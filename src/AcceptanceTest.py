import unittest
import subprocess

class AcceptanceTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_2a(self):
        bashCmd = "cat powerInput.txt | ./power"
        process = subprocess.Popen(bashCmd,shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        self.assertIsNone(error)
        self.assertEqual(output.decode("utf-8"),"Stav site: ERROR\n")



if __name__ == '__main__':
    unittest.main()
