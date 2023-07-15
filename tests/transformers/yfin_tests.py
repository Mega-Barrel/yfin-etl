"""yFinETL test file"""

import unittest
from unittest.mock import (
    patch,
    MagicMock
)

import pandas as pd
from yfin.transformers.yfin_transformer import YfinETL

class YfinETLTests(unittest.TestCase):
    """
    Class for testing individual functions
    """

    def setUp(self):
        self.etl = YfinETL('AAPL', '2021-01-01', '2021-12-31')

    def tearDown(self) -> None:
        pass

    def test_extract(self):
        """
        Testing extract function
        """
        with patch('yfin_etl.yf.download') as mock_download:
            mock_download.return_value = MagicMock()
            result = self.etl.extract()
            self.assertIsNone(result)
            self.assertNotEqual(result, False)

    # def test_transform_empty_dataframe(self):
    #     """
    #     Test case, when data_frame is empty
    #     """
    #     data_frame = pd.DataFrame()
    #     result = self.etl.transform(data_frame)
    #     self.assertTrue(result.empty)

    # def test_transform_non_empty_dataframe(self):
    #     """
    #     Test case, when data_frams is passed
    #     """
    #     data_frame = self.etl.extract()
    #     result = self.etl.transform(data_frame)

if __name__ == '__main__':
    unittest.main()
