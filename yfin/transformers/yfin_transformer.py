"""Yfin ETL Component"""

import pandas as pd     # pylint: disable=E0401
import yfinance as yf   # pylint: disable=E0401
from yfin.common.sqlite import YfinDB
from yfin.common.yfin_logger import logger
from yfin.common.time_logger import time_it

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
        # Creating YfinDB object
        self.ticker_db = YfinDB()
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    @time_it
    def extract(self):
        """
        Download daily ticker data from yahoo finance
        """
        try:
            logger.info('Process started for function: extract..')
            # Get new data from yfin
            logger.info(
                'Extracting data from Date: %s to \
                Date: %s for ticker: %s',
                self.start_date, self.end_date, self.symbol
            )
            ticker_df = yf.download(
                self.symbol,
                start = self.start_date,
                end = self.end_date,
                interval='1d',
                threads=True
            ).reset_index()
            return ticker_df
        except Exception as error: # pylint: disable=W0718
            logger.error('Error occured while extracting data')
            logger.error(error)
            return False
        finally:
            logger.info('Process completed for function: extract..')

    @time_it
    def transform(self, data_frame: pd.DataFrame):
        """
        Applies the necessary transformation to create report 1
        
        :param data_frame: Pandas DataFrame as Input
        
        :returns:
            data_frame: Transformed Pandas DataFrame as Output
        """
        logger.info('Process started for function: transform..')
        if data_frame.empty:
            logger.debug('The dataframe is empty. No transformations will be applied.')
            return data_frame
        logger.info('Applying transformations to yfin source data')
        data_frame['% Change'] = round(
            data_frame['Adj Close'] / data_frame['Adj Close'].shift(1) - 1,
            4
        )
        logger.info('Process completed for function: transform..')
        return data_frame

    @time_it
    def load(self, data_frame: pd.DataFrame) -> None:
        """
        Saves transform DataFrame to target DB

        :param data_frame: Pandas DataFrame as a Input
        """
        # Connection to PostgreSQL DB
        logger.info('Process started for function: load..')
        if data_frame.empty:
            logger.debug('The dataframe is empty. Skipping data load operation')
        else:
            try:
                logger.info('Loading %s data into DB.', self.symbol)
                # If table exists append to the new data to table
                self.ticker_db.insert_ticker_data(self.symbol, data_frame)
                logger.info('Ticker: %s data inserted successfully!', self.symbol)
            except Exception as error: # pylint: disable=W0718
                # Print Error message
                logger.debug('Error occured while performing load operation')
                logger.error(error)
            finally:
                logger.info('Process completed for function: load..')

    @time_it
    def etl_report(self):
        """
        Call the Extract, transform, and load method for ticker
        """
        try:
            logger.info('Process started for function: etl_report..')
            logger.info('extract function called!')
            # Extraction
            data_frame = self.extract()
            # Apply transformation
            logger.info('transform function called!')
            data_frame = self.transform(data_frame=data_frame)
            # # Load the data to DB
            logger.info('load function called!')
            self.load(data_frame=data_frame)
            return True
        except Exception as error: # pylint: disable=W0718
            logger.error('Error occured in function: etl_report')
            logger.error(error)
            return False
        finally:
            logger.info('Process completed for function: etl_report..')
