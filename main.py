"""Main file for Yfin ETL"""

from yfin.common.yfin_logger import logger
from yfin.common.time_logger import time_it
from yfin.transformers.yfin_transformer import YfinETL

@time_it
def main():
    """
    Main function
    """
    try:
        logger.info('Process Started for function: main ')

        # Input Params
        ticker = 'AAPL'
        start_date = '2020-01-01'
        end_date = '2023-05-31'

        # aCreating YfinETL object
        data = YfinETL(ticker, start_date=start_date, end_date=end_date)
        data.etl_report()
        logger.info('Process Completed for funtion: main')
    except Exception as error: #pylint: disable=W0718
        logger.error('Error occured in function: etl_report')
        logger.error(error)

if __name__ == "__main__":
    main()
