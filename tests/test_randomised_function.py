import unittest
from lecture import randomised_function, is_small
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('lecture.is_small')
    def test_randomised_function(self, mock_is_small):
        mock_is_small.return_value = True
        self.assertEqual('software', randomised_function())
