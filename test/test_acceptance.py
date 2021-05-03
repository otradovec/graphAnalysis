import unittest
import subprocess


class AcceptanceTest(unittest.TestCase):
    def cmd_test(self, bashCmd, expected_result):
        process = subprocess.Popen(bashCmd, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode("utf-8")
        self.assertIsNone(error)
        if type(expected_result) == str:
            self.assertEqual(output, expected_result)
        else:
            self.assertIn(output, expected_result)

    def test_2a(self):
        bashCmd = "cat resources/powerInput.txt | ./power"
        expected_result = "Stav site: ERROR\n"
        self.cmd_test(bashCmd, expected_result)

    def test_2a_2(self):
        bashCmd = "cat resources/powerInput2.txt | ./power"
        expected_result = "Stav site: OK\n"
        self.cmd_test(bashCmd, expected_result)

    def test_2b(self):
        bashCmd = "cat resources/powerInput.txt | ./reset"
        expected_result = "T02 - T04: 2\nT02 - T03: 10\nT01 - T02: 15\nHodnoceni: 27\n"
        self.cmd_test(bashCmd, expected_result)

    def test_2c(self):
        bashCmd = "cat resources/weaknessInput.txt | ./weakness"
        expected_result = "T02 - T04\nT02 - T05\nT02\n"
        self.cmd_test(bashCmd, expected_result)

    def test_2d(self):
        bashCmd = "cat resources/avltreeInput.txt | ./avltree"
        expected_result = "5\n5|_ 15\n9|5 15\n9|5 15|_ 5 _ _\n9|5 15|_ 5 _ 155\n"
        # self.cmd_test(bashCmd,expected_result)

    def test_3a(self):
        bashCmd = "cat resources/messageInput.txt | ./message"
        expected_result = "Vy: 0\nPepa: 2\nHonza: 3\nAnna: 3\nMichal: 4\nOndra: 5\nTomas: 6\nJirka: 6\n"
        self.cmd_test(bashCmd, expected_result)

    def test_3b(self):
        bashCmd = "cat resources/forestInput.txt | ./forest"
        expected_result = ["A -> B -> C -> D: 4\n",
                           "A -> B -> D -> C: 4\n",
                           "C -> D -> B -> A: 4\n",
                           "D -> C -> B -> A: 4\n",
                           "C -> D -> A -> B: 5\n",
                           "B -> A -> D -> C: 5\n",
                           "D -> C -> A -> B: 5\n",
                           "B -> A -> C -> D: 5\n",
                           "A -> D -> C -> B: 6\n",
                           "B -> C -> D -> A: 6\n",
                           "D -> A -> B -> C: 6\n",
                           "C -> B -> A -> D: 6\n"]
        self.cmd_test(bashCmd, expected_result)

    def test_3c(self):
        bash_cmd = "cat resources/raceInput.txt | ./race"
        expected_result = "A -> B -> C -> D: 3\n"
        self.cmd_test(bash_cmd, expected_result)


if __name__ == '__main__':
    unittest.main()
