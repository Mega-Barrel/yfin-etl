"""Yfin ETL Component"""
import pandas as pd
import yfinance as yf
from yfin.common.sqlite import YfinDB

class YfinETL():
    """
    Read the Yfin data for specific ticker, transforms and write
    the transformed data to postgreSQL DB
    """
    def __init__(
        self,
        symbol,
        start_date,
        end_date
    ):
        """
        Constructor for YfinTransformer

        :param symbol: Stock ticker name
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        # Creating YfinDB object
        self.ticker_db = YfinDB()

    def extract(self):
        """
        Download daily ticker data from yahoo finance
        """
        try:
            # Get new data from yfin
            ticker_df = yf.download(
                self.symbol,
                start = self.start_date,
                end = self.end_date,
                interval='1d',
                threads=True
            ).reset_index()
            return ticker_df
        except: # pylint: disable=W0702
            print('Invalid Ticker name passed')

    def transform(self, data_frame: pd.DataFrame):
        """
        Applies the necessary transformation to create report 1
        
        :param data_frame: Pandas DataFrame as Input
        
        :returns:
            data_frame: Transformed Pandas DataFrame as Output
        """
        if data_frame.empty:
            print('The dataframe is empty. No transformations will be applied.')
            return data_frame
        print('Applying transformations to yfin source data')
        data_frame['% Change'] = round(
            data_frame['Adj Close'] / data_frame['Adj Close'].shift(1) - 1,
            4
        )
        return data_frame

    def load(self, data_frame: pd.DataFrame) -> None:
        """
        Saves transform DataFrame to target DB

        :param data_frame: Pandas DataFrame as a Input
        """
        # Connection to PostgreSQL DB
        if data_frame.empty:
            print('Empty DataFrame.')
            print('Skipping data load operation')
        else:
            try:
                # If table exists append to the new data to table
                self.ticker_db.insert_ticker(self.symbol, data_frame)
                print(f"Ticker: {self.symbol} data inserted successfully!")
            except: # pylint: disable=W0702
                # Print Error message
                print('Error occured while performing load operation')

    def etl_report(self):
        """
        Call the Extract, transform, and load method for ticker
        """
        try:
            # Extraction
            data_frame = self.extract()
            # Apply transformation
            data_frame = self.transform(data_frame=data_frame)
            # Load the data to DB
            self.load(data_frame=data_frame)
            return True
        except: # pylint: disable=W0702
            print('One or more parameter entered wrong!!')
            print('Check your input')
