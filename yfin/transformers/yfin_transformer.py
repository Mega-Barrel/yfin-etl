"""Yfin ETL Component"""
import pandas as pd
import yfinance as yf

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

    def extract(self):
        """
        Download daily ticker data from yahoo finance
        """
        try:
            # Get new data from yfin
            ticker_df = yf.download(self.symbol, interval='1mo', threads=True).reset_index()
            return ticker_df
        except: # pylint: disable=W0702
            return 'Invalid Ticker name.'

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
            2
        )
        return data_frame

    def load(self, data_frame: pd.DataFrame) -> None:
        """
        Saves transform DataFrame to target DB

        :param data_frame: Pandas DataFrame as a Input
        """
        # Connection to PostgreSQL DB
        print(data_frame)
        # return data_frame

    def etl_report(self):
        """
        Call the Extract, transform, and load method for ticker
        """
        # Extraction
        data_frame = self.extract()
        # Apply transformation
        data_frame = self.transform(data_frame=data_frame)
        # Load the data to DB
        self.load(data_frame=data_frame)
        return True
