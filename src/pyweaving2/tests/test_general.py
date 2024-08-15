import unittest
from pyweaving2.wif import WIFReader
from pyweaving2 import cmd
from pathlib import Path
# from src import
import os

# get path of module to find test file in data folder
lpath = Path(os.path.realpath(__file__)).parent
test_data_path  = lpath / 'data'
test_data_path  = test_data_path.resolve()

test_file = test_data_path / 'schort.wif'
test_file_rror_extension = test_file / 'schort.wf'
test_file_error_name = test_file / 'schrt.wif'
test_out_file = test_data_path / 'tmp.wif'


# test arguments
test_arguments = [
    # {'command': 'ext_error', 'args': ['prog', 'render', str(test_file)], 'result': 'normal'},
    {'command' :'empty',      'args' :['prog'],             'result': 'exit'},
    {'command': 'weave_only', 'args' : ['prog', 'weave'],     'result':'exit'},
    {'command': 'render_only', 'args' : ['prog', 'render'],   'result':'exit'},
    {'command': 'thread_only', 'args' : ['prog', 'thread'],   'result':'exit'},
    {'command': 'tie_up_only', 'args' :  ['prog', 'tie_up'],  'result':'exit'},
    {'command': 'stats_only', 'args': ['prog', 'stats'],      'result': 'exit'},
    {'command': 'convert_only', 'args': ['prog', 'convert'],  'result': 'exit'},
    # {'command': 'weave', 'args': ['prog', 'weave', str(test_file)], 'result': 'break'},
    # {'command': 'render', 'args': ['prog', 'render', str(test_file)], 'result': 'exit'},
    # {'command': 'thread', 'args': ['prog', 'thread', str(test_file)], 'result': 'exit'},
    {'command': 'tie_up', 'args': ['prog', 'tie_up', str(test_file)], 'result': 'exit'},
    {'command': 'stats', 'args': ['prog', 'stats', str(test_file)], 'result': 'normal'},
    # {'command': 'convert', 'args': ['prog', 'convert', str(test_file), str(test_out_file)], 'result': 'exit'},
    {'command': 'convert', 'args': ['prog', 'convert', str(test_file)], 'result': 'exit'},
    {'command': 'filename error', 'args': ['prog', 'convert', str(test_file_error_name)], 'result': 'exit'}

]


class MyTestCase(unittest.TestCase):
    def test_wif_reader(self):

        self.assertEqual(test_file.exists(), True, f'No test file found on {str(testfile)}')
        draft_object = WIFReader(test_file).read()

        # self.assertEqual(type(draft_object), type())  # add assertion here

class CliTestCases(unittest.TestCase):
    def test_cli_arguments(self):
        for test in test_arguments:
            if test['result'] == 'break':  # we expect a break
                with self.assertRaises(Exception) as context:
                    cmd.main(argv=test['args'])

                self.assertTrue('only liftplan' in str(context.exception), f'test: {test["command"]} did not fail on liftplan')
            elif test['result'] == 'exit':
                with self.assertRaises(SystemExit) as cm:
                    cmd.main(argv=test['args'])

                self.assertEqual(cm.exception.code, 2, f'failed on {test["command"]}' )
            elif test['result'] == 'normal':
                ans = cmd.main(argv=test['args'])
                self.assertTrue(ans is None, f'test missed:  {test["command"]}' )
            elif test['result']  == 'assert':
                pass



if __name__ == '__main__':
    unittest.main()
