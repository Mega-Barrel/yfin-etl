"""Yfin SQLite Component"""

import sqlite3
from yfin.common.time_logger import time_it
from yfin.common.yfin_logger import logger

class YfinDB():
    """
    Class to handle all DB related operations
    """

    def __init__(self):
        """
        Initialize _db and _cursor
        """
        logger.info('Created connection with DB..')
        self._engine = sqlite3.connect('db/ticker.db')

    @time_it
    def insert_ticker_data(self, table_name, data_frame):
        """
        Insert ticker DataFrame to sqlite table

        :param table_name: Table name
        :param data_frame: Pandas data_frame
        """
        try:
            logger.info('Process started for function: insert_ticker_data..')
            data_frame.to_sql(
                table_name,
                self._engine,
                if_exists='append',
                index=False
            )
            logger.info('Data Inserted to %s Table.', table_name)
            return True
        except Exception as error: # pylint: disable=W0718
            logger.error('Error occured while inserting data')
            logger.error(error)
            return False
        finally:
            logger.info('Process completed for function: connect..')
