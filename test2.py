from mymodule import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        rm("./lol")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("./lol")