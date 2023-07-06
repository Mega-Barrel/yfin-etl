# Main file for Yfin ETL

The Main file for Yfin ETL is a Python script that serves as the entry point for running the Yfin ETL process. It calls the necessary functions and classes to perform the extraction, transformation, and loading of stock ticker data from Yahoo Finance into a PostgreSQL database.

## Prerequisites

Before using the Main file for Yfin ETL, ensure that you have the following dependencies installed:

- **yfin.common.yfin_logger:** This module should be available in your project's directory.
- **yfin.common.time_logger:** This module should be available in your project's directory.
- **yfin.transformers.yfin_transformer:** This module should be available in your project's directory.

## Usage

To use the Main file for Yfin ETL, follow these steps:

1. Implement the main function with the necessary logic for running the ETL process:
```python
def main():
    try:
        logger.info('Process Started for function: main ')

        # Input Params
        ticker = 'AAPL'
        start_date = '2020-01-01'
        end_date = '2023-05-31'

        # Creating YfinETL object
        data = YfinETL(ticker, start_date=start_date, end_date=end_date)
        data.etl_report()
        logger.info('Process Completed for function: main')
    except Exception as error:
        logger.error('Error occurred in function: etl_report')
        logger.error(error)
```

2. Call the main function if the script is run directly:
```python
if __name__ == "__main__":
    main()
```

This ensures that the main function is executed only when the script is run as the main entry point.

## Error Handling
- The Main file for Yfin ETL catches exceptions that occur during the ETL process. 
- If an error occurs, it logs the error message using the logger.error function. 
- You can check the logs for detailed error information.

## License
This project is licensed under the MIT License.