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
        bashCmd = "cat resources/powerInput.txt | ./reset"
        expectedResult = "T02 - T04: 2\nT02 - T03: 10\nT01 - T02: 15\nHodnoceni: 27\n"
        self.cmd_test(bashCmd,expectedResult)

    def test_2c(self):
        bashCmd = "cat resources/weaknessInput.txt | ./weakness"
        expectedResult = "T02 - T04\nT02 - T05\nT02\n"
        self.cmd_test(bashCmd,expectedResult)

if __name__ == '__main__':
    unittest.main()
