# Yfin ETL Component

The Yfin ETL Component is a Python class that allows you to extract, transform, and load (ETL) stock ticker data from Yahoo Finance into a PostgreSQL database. It provides methods to perform each step of the ETL process.

## Prerequisites

Before using the Yfin ETL Component, ensure that you have the following dependencies installed:

- pandas: `pip install pandas`
- yfinance: `pip install yfinance`
- yfin.common.sqlite: This module should be available in your project's directory.
- yfin.common.yfin_logger: This module should be available in your project's directory.
- yfin.common.time_logger: This module should be available in your project's directory.

## Usage

To use the Yfin ETL Component, follow these steps:

1. Importing the necessary modules:

```python
import pandas as pd
import yfinance as yf
from yfin.common.sqlite import YfinDB
from yfin.common.yfin_logger import logger
from yfin.common.time_logger import time_it
```

## Methods
The YfinETL class provides the following methods:

**extract():** 
- Downloads the daily ticker data from Yahoo Finance for the specified  symbol, start date, and end date. 
- Returns a Pandas DataFrame containing the data.

**transform(data_frame):** 
- Applies necessary transformations to the input DataFrame. 
- Adds a "% Change" column that calculates the percentage change in the "Adj Close" column compared to the previous day. 
- Returns the transformed DataFrame.

**load(data_frame):** 
- Saves the transformed DataFrame to the target PostgreSQL database. 
- If the DataFrame is empty, the load operation is skipped.

**etl_report():** 
- Performs the complete ETL process by calling the extract, transform, and load methods. 
- Returns True if the process is successful, False otherwise.

## Error Handling
The Yfin ETL Component handles exceptions during the ETL process. If an error occurs, it logs the error message and returns False. You can check the logs for detailed error information.

## License
This project is licensed under the MIT License.