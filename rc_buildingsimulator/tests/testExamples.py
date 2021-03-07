import sys
import os
from pathlib import Path
import unittest

EXAMPLES = Path(__file__).parents[1] / "examples"

class TestBuildingSim(unittest.TestCase):

    def test_annualSimulation(self):
        runfile = open(EXAMPLES / 'annualSimulation.py')
        exec(runfile.read())
        runfile.close()

    def test_annualSimulation_importRadiation(self):
        runfile = open(EXAMPLES / 'annualSimulation_importRadiation.py')
        exec(runfile.read())
        runfile.close()

    def test_calculateRadiation(self):
        runfile = open(EXAMPLES / 'calculateRadiation.py')
        exec(runfile.read())
        runfile.close()

    def test_hourSimulation(self):
        runfile = open(EXAMPLES / 'hourSimulation.py')
        exec(runfile.read())
        runfile.close()

    def test_sunAngles(self):
        runfile = open(EXAMPLES / 'sunAngles.py')
        exec(runfile.read())
        runfile.close()


if __name__ == '__main__':
    unittest.main()
