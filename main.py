"""Main file for Yfin ETL"""

from yfin.transformers.yfin_transformer import YfinETL

if __name__ == "__main__":
    TICKER = ['GOOG']
    START_DATE = '2022-01-01'
    END_DATE = '2023-01-10'
    data = YfinETL(TICKER, START_DATE, END_DATE)
    data.etl_report()
