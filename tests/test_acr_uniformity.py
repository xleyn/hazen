import os
import unittest
import pathlib
import pydicom
import numpy as np

from hazenlib.tasks.acr_uniformity import ACRUniformity
from hazenlib.acr_tools import ACRTools
from tests import TEST_DATA_DIR, TEST_REPORT_DIR


class TestACRUniformitySiemens(unittest.TestCase):
    ACR_UNIFORMITY_DATA = pathlib.Path(TEST_DATA_DIR / 'acr')
    piu = 67.95

    def setUp(self):
        self.acr_uniformity_task = ACRUniformity(data_paths=[os.path.join(TEST_DATA_DIR, 'acr')],
                                                 report_dir=pathlib.PurePath.joinpath(TEST_REPORT_DIR))

        self.acr_uniformity_task.ACR_obj = ACRTools(
            [pydicom.read_file(os.path.join(TEST_DATA_DIR, 'acr', 'Siemens', f'{i}')) for i in
             os.listdir(os.path.join(TEST_DATA_DIR, 'acr', 'Siemens'))])

        self.dcm = self.acr_uniformity_task.ACR_obj.dcm[6]

    def test_uniformity(self):
        results = self.acr_uniformity_task.get_integral_uniformity(self.dcm)
        assert round(results, 2) == self.piu


# class TestACRUniformityPhilips(unittest.TestCase):
#
class TestACRUniformityGE(unittest.TestCase):
    ACR_UNIFORMITY_DATA = pathlib.Path(TEST_DATA_DIR / 'acr')
    piu = 85.17

    def setUp(self):
        self.acr_uniformity_task = ACRUniformity(data_paths=[os.path.join(TEST_DATA_DIR, 'acr')],
                                                 report_dir=pathlib.PurePath.joinpath(TEST_REPORT_DIR))
        self.acr_uniformity_task.ACR_obj = ACRTools(
            [pydicom.read_file(os.path.join(TEST_DATA_DIR, 'acr', 'GE', f'{i}')) for i in
             os.listdir(os.path.join(TEST_DATA_DIR, 'acr', 'GE'))])

        self.dcm = self.acr_uniformity_task.ACR_obj.dcm[6]

    def test_uniformity(self):
        results = self.acr_uniformity_task.get_integral_uniformity(self.dcm)
        assert round(results, 2) == self.piu
