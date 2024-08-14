import unittest
from pyweaving2.wif import WIFReader
from pyweaving2 import cmd
from pathlib import Path
# from src import
import os

lpath = Path(os.path.realpath(__file__)).parent
testfile = lpath / 'data' / 'schort.wif'
testfile = testfile.resolve()

# test arguments
test_arguments = [
    {'command' :'empty',      'args' :['prog'],             'result': 'exit'},
    {'command': 'weave_only', 'args' : ['prog', 'weave'],     'result':'exit'},
    {'command': 'render_only', 'args' : ['prog', 'render'],   'result':'exit'},
    {'command': 'thread_only', 'args' : ['prog', 'thread'],   'result':'exit'},
    {'command': 'tie_up_only', 'args' :  ['prog', 'tie_up'],  'result':'exit'},
    {'command': 'stats_only', 'args': ['prog', 'stats'],      'result': 'exit'},
    {'command': 'convert_only', 'args': ['prog', 'convert'],  'result': 'exit'},
    {'command': 'weave', 'args': ['prog', 'weave', 'schort.wif'], 'result': 'exit'},
    {'command': 'render', 'args': ['prog', 'render', 'schort.wif'], 'result': 'exit'},
    {'command': 'thread', 'args': ['prog', 'thread', 'schort.wif'], 'result': 'exit'},
    {'command': 'tie_up', 'args': ['prog', 'tie_up', 'schort.wif'], 'result': 'exit'},
    {'command': 'stats', 'args': ['prog', 'stats', 'schort.wif'], 'result': 'exit'},
    {'command': 'convert', 'args': ['prog', 'convert', 'schort.wif'], 'result': 'exit'}
]


class MyTestCase(unittest.TestCase):
    def test_wif_reader(self):

        self.assertEqual(testfile.exists(), True, f'No test file found on {str(testfile)}')
        draft_object = WIFReader(testfile).read()

        # self.assertEqual(type(draft_object), type())  # add assertion here

class CliTestCases(unittest.TestCase):
    def test_cli_arguments(self):
        for test in test_arguments:
            if test['result'] == 'break':  # we expect a break
                with self.assertRaises(Exception) as context:
                    cmd.main(argv=test['args'])

                self.assertTrue('This is broken' in str(context.exception), f'test: {test["command"]} failed')
            if test['result'] == 'exit':
                with self.assertRaises(SystemExit) as cm:
                    cmd.main(argv=test['args'])

                self.assertEqual(cm.exception.code, 2, f'failed on {test["command"]}' )


if __name__ == '__main__':
    unittest.main()
