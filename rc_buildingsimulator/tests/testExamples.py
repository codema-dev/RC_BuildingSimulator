from pathlib import Path
import unittest
from unittest.mock import patch

EXAMPLES = Path(__file__).parents[1] / "examples"


@patch("matplotlib.pyplot.show")
class TestBuildingSim(unittest.TestCase):

    def test_annualSimulation(self, mock_show):
        import rc_buildingsimulator.examples.annualSimulation

    def test_annualSimulation_importRadiation(self, mock_show):
        import rc_buildingsimulator.examples.annualSimulation_importRadiation

    def test_calculateRadiation(self, mock_show):
        import rc_buildingsimulator.examples.calculateRadiation

    def test_hourSimulation(self, mock_show):
        import rc_buildingsimulator.examples.hourSimulation

    def test_sunAngles(self, mock_show):
        import rc_buildingsimulator.examples.sunAngles

if __name__ == '__main__':
    unittest.main()
