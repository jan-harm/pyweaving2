import pytest
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


class TestCase():

    def test_wif_reader(self):

        assert test_file.exists() , f'No test file found on {str(test_file)}'
        draft_object = WIFReader(test_file).read()

        # self.assertEqual(type(draft_object), type())  # add assertion here

class TestCliCases():
    @pytest.mark.parametrize('test_args', test_arguments)
    def test_cli_arguments(self, test_args):
        for test in test_arguments:
            if test['result'] == 'break':  # we expect a break
                with pytest.raises(Exception) as context:
                    cmd.main(argv=test['args'])

            elif test['result'] == 'exit':
                with pytest.raises(SystemExit) as cm:
                    cmd.main(argv=test['args'])

                assert cm.value.code ==2, f'failed on {test["command"]}'
            elif test['result'] == 'normal':
                ans = cmd.main(argv=test['args'])
                assert ans is None, f'test missed:  {test["command"]}'
            elif test['result']  == 'assert':
                pass


