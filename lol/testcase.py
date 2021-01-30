from mymodule import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")
        
    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

# Hasil testcase masih salah, sorry belum bisa dijalankan
# from mymodule import rm

# import mock
# import unittest

# class RmTestCase(unittest.TestCase):
    
#     @mock.patch('mymodule.os')
#     def test_rm(self, mock_os):
#         rm("any path")
#         # test that rm called os.remove with the right parameters
#         mock_os.remove.assert_called_with("any path")