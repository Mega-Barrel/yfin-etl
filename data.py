""" Code file to connect to request Yfin data"""
import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

def get_data(symbol, start='2023-01-01'):
    '''
    Get data from yfin.

    @param: symbol: Ticker name
    '''
    try:
        # read max_date from existing symbol table
        max_date = pd.read_sql(f'SELECT MAX(Date) FROM {symbol}', engine).values[0][0]
        # Get new data from yfin
        new_data = yf.download(symbol, start=pd.to_datetime(max_date))
        new_rows = new_data[new_data.index > max_date]

        # Append new data to the existing table
        new_rows.to_sql(symbol, engine, if_exists='append')
        print(str(len(new_rows)) + ' rows imported to DB')

    except: # pylint: disable=W0702
        new_data = yf.download(symbol, start=start)
        new_data.to_sql(symbol, engine)
        print(f'New table created for {symbol} with {str(len(new_data))} rows')

if __name__ == '__main__':
    # create database engine
    engine = create_engine('sqlite:///stock_DB.db')
    # Data to extract
    symbol = 'MSFT'
    get_data(symbol)
