import unittest
import pathlib

import hazenlib.uniformity as hazen_uniformity
from tests import TEST_DATA_DIR


class TestUniformity(unittest.TestCase):

    UNIFORMITY_DATA = pathlib.Path(TEST_DATA_DIR / 'uniformity')
    IPEM_HORIZONTAL = 1.0
    IPEM_VERTICAL = 0.98125

    def setUp(self):
        self.test_file = [str(self.UNIFORMITY_DATA / 'axial_oil.IMA')]

    def test_uniformity(self):
        results = hazen_uniformity.main(self.test_file)

        assert results['uniformity']['horizontal']['IPEM'] == self.IPEM_HORIZONTAL
        assert results['uniformity']['vertical']['IPEM'] == self.IPEM_VERTICAL


class TestSagUniformity(TestUniformity):
    IPEM_HORIZONTAL = 0.46875
    IPEM_VERTICAL = 0.5125

    def setUp(self):
        self.test_file = [str(self.UNIFORMITY_DATA / 'sag.dcm')]


class TestCorUniformity(TestUniformity):
    IPEM_HORIZONTAL = 0.35
    IPEM_VERTICAL = 0.45

    def setUp(self):
        self.test_file = [str(self.UNIFORMITY_DATA / 'cor.dcm')]