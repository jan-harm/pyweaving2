import unittest
from pyweaving2.wif import WIFReader
from pathlib import Path
# from src import
import os

lpath = Path(os.path.realpath(__file__)).parent
testfile = lpath / 'data' / 'schort.wif'
testfile = testfile.resolve()


class MyTestCase(unittest.TestCase):
    def test_wif_reader(self):

        self.assertEqual(testfile.exists(), True, f'No test file found on {str(testfile)}')
        draft_object = WIFReader(testfile).read()

        # self.assertEqual(type(draft_object), type())  # add assertion here



if __name__ == '__main__':
    unittest.main()
