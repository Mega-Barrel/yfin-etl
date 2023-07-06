# Yfin PostgreSQL Component

The Yfin PostgreSQL Component is a Python class that provides functionality to handle database operations for storing ticker data. It uses SQLite as the underlying database engine and allows you to insert ticker data from a Pandas DataFrame into a specified table.

## Prerequisites

Before using the Yfin PostgreSQL Component, ensure that you have the following dependencies installed:

- sqlite3: This module is included in Python's standard library.
- yfin.common.time_logger: This module should be available in your project's directory.
- yfin.common.yfin_logger: This module should be available in your project's directory.

## Usage

To use the Yfin PostgreSQL Component, follow these steps:

1. Import the necessary modules:

```python
import sqlite3
from yfin.common.time_logger import time_it
from yfin.common.yfin_logger import logger
```

## Methods
The YfinDB class provides the following method:

**insert_ticker_data(table_name, data_frame)**: 
- Inserts the provided Pandas DataFrame data_frame into the specified SQLite table_name. 
- The data is appended to the table if it already exists. 
- Returns True if the insertion is successful, False otherwise.

## Error Handling
- The Yfin PostgreSQL Component handles exceptions during the database operations. 
- If an error occurs, it logs the error message and returns False. 
- You can check the logs for detailed error information.

## Database Connection
- The YfinDB class establishes a connection with the SQLite database file specified as 'db/ticker.db' in the class's constructor. 
- Make sure that the database file exists in the specified location or modify the connection string accordingly.

## License
This project is licensed under the MIT License.