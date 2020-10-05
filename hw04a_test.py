"""
this is the unit test file of hw04a
"""
from hw04a import get_usr_repo
import unittest

class HW04aTest(unittest.TestCase):
    def test_testcase_1(self):
        self.assertEqual(get_usr_repo("usr_id"),[])
        
if __name__ == '__main__':
    unittest.main()