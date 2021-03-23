import unittest
import subprocess

class AcceptanceTest(unittest.TestCase):
    def cmd_test(self,bashCmd,expectedResult):
        process = subprocess.Popen(bashCmd,shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        self.assertIsNone(error)
        self.assertEqual(output.decode("utf-8"),expectedResult)

    def test_2a(self):
        bashCmd = "cat resources/powerInput.txt | ./power"
        expectedResult = "Stav site: ERROR\n"
        self.cmd_test(bashCmd,expectedResult)

    def test_2a_2(self):
        bashCmd = "cat resources/powerInput2.txt | ./power"
        expectedResult = "Stav site: OK\n"
        self.cmd_test(bashCmd,expectedResult)

    def test_2b(self):
        pass


if __name__ == '__main__':
    unittest.main()
