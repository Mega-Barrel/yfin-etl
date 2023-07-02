"""Yfin PostgreSQL Component"""
import sqlite3
import pandas as pd # pylint: disable=E0401

class YfinDB():
    """
    Class to handle all DB related operations
    """

    def __init__(self):
        """
        Initialize _db and _cursor
        """
        self._engine = self.connect()

    def connect(self):
        """
        returns PG connection object
        """
        # create and return PG engine
        print('Connection created')
        return sqlite3.connect('db/ticker.db')

    def insert_ticker(self, table_name, data_frame):
        """
        Insert ticker DataFrame to sqlite table

        :param table_name: Pandas DataFrame
        :param data_frame: Ticker price data
        """
        try:
            data_frame.to_sql(
                table_name,
                self._engine,
                if_exists='append',
                index=False
            )
            print(f'Data Inserted to {table_name} Table.')
            return True
        except Exception as error: # pylint: disable=W0718
            print(error)
            print('Error while performing inserting operation')

    # TODO: Add max_date filter to download latest data
    def get_max_date(self, ticker_name: str):
        """
        Get's the last/max date for the ticker specified
        
        :param ticker_name: Ticker name
        """
        query = f"""
            SELECT
                MAX(Date)
            FROM
                {ticker_name}
        """
        max_date = pd.read_sql(query, self._engine).values[0][0]
        return max_date
